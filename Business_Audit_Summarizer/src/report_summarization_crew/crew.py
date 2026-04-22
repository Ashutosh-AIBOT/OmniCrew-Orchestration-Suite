import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Load environment variables
load_dotenv()

# Define the High-Speed NVIDIA LLM
nvidia_llm = LLM(
    model="meta/llama-3.1-8b-instruct",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# Define absolute paths for config files
base_path = os.path.dirname(os.path.abspath(__file__))
agents_config_path = os.path.join(base_path, "config/agents.yaml")
tasks_config_path = os.path.join(base_path, "config/tasks.yaml")

@CrewBase
class ReportSummarizationCrew():
    """ReportSummarizationCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # set the paths for config files using ABSOLUTE PATHS
    agents_config = agents_config_path
    tasks_config = tasks_config_path
    
    # define the agents
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"],
            verbose=True,
            llm=nvidia_llm
        )
        
    @agent
    def report_summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config["report_summarizer"],
            verbose=True,
            llm=nvidia_llm
        )
        
    # define the tasks
    @task
    def report_generation_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_generation_task"]
        )
        
    @task
    def report_summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_summarization_task"]
        )
        
    # define the crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False,
            planning=False
        )