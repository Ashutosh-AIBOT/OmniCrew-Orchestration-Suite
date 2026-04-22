import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool

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

# define the search tool
search_tool = SerperDevTool()

@CrewBase
class NewsReportCrew():
    """NewsReportCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # set the paths for config files using ABSOLUTE PATHS
    agents_config = agents_config_path
    tasks_config = tasks_config_path
    
    # define the agent
    @agent
    def news_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config["news_reporter"],
            verbose=True,
            tools=[search_tool],
            llm=nvidia_llm
        )
        
    # define the task
    @task
    def news_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["news_report_task"]
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