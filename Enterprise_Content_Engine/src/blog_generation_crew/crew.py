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

# define the web search tool
web_search_tool = SerperDevTool()

@CrewBase
class BlogGenerationCrew():
    """BlogGenerationCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # set the path of config files using ABSOLUTE PATHS
    agents_config = agents_config_path
    tasks_config = tasks_config_path
    
    # define the agents inside the crew
    @agent
    def research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_agent"],
            verbose=True,
            allow_delegation=False,
            tools=[web_search_tool],
            llm=nvidia_llm
        )
        
    @agent
    def blog_writing_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writing_agent"],
            verbose=True,
            allow_delegation=False,
            llm=nvidia_llm
        )
        
    @agent
    def blog_review_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_review_agent"],
            verbose=True,
            allow_delegation=False,
            llm=nvidia_llm
        )

    # Define the 3 tasks
    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"]
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"]
        )
        
    @task
    def review_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_task"]
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.research_agent(),
                    self.blog_writing_agent(),
                    self.blog_review_agent()],
            tasks=[self.research_task(),
                   self.blog_writing_task(),
                   self.review_task()],
            process=Process.sequential, # High-Speed Pipeline
            verbose=True,
            memory=False, 
            planning=False 
        )