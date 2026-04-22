import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

# Load environment variables
load_dotenv()

# Configure NVIDIA NIM (OpenAI-compatible)
os.environ["OPENAI_API_BASE"] = "https://integrate.api.nvidia.com/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("NVIDIA_API_KEY")

# Define the shared LLM
nvidia_llm = "openai/meta/llama-3.1-70b-instruct"


@CrewBase
class WritingCrew():
    """WritingCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # define the path of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # ======================== Agents ========================
    # define agents
    @agent
    def technical_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["technical_writer"],
            llm=nvidia_llm
        )
    
    @agent
    def content_editor(self) -> Agent:
        return Agent(
            config=self.agents_config["content_editor"],
            llm=nvidia_llm
        )

    # ======================== Tasks ===========================
    # define the tasks
    @task
    def write_getting_started_guide(self) -> Task:
        return Task(
            config=self.tasks_config["write_getting_started_guide"]
        )
        
    @task
    def review_and_polish_guide(self) -> Task:
        return Task(
            config=self.tasks_config["review_and_polish_guide"]        
            )
    
    # ======================== Crew ==============================
    # define the crew
    @crew
    def crew(self) -> Crew:
        """Creates the WritingCrew crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )
