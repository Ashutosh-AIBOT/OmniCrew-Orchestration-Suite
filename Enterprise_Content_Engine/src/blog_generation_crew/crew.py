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
# We use 'openai/' prefix with base_url to use NVIDIA's OpenAI-compatible API
nvidia_llm = LLM(
    model="openai/meta/llama-3.1-8b-instruct",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# define the web search tool
web_search_tool = SerperDevTool()

@CrewBase
class BlogGenerationCrew():
    """BlogGenerationCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    # set the path of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # define the agents inside the crew
    @agent
    def team_leader(self) -> Agent:
        return Agent(
            config=self.agents_config["team_leader"],
            verbose=True,
            allow_delegation=True,
            llm=nvidia_llm
        )
        
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

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="blog.md"
        )
        
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.research_agent(),
                    self.blog_writing_agent(),
                    self.blog_review_agent()],
            tasks=[self.blog_writing_task()],
            process=Process.hierarchical,
            verbose=True,
            manager_agent=self.team_leader(),
            memory=False, # DISABLED to prevent OpenAI embedding calls
            planning=False # DISABLED to prevent OpenAI planning calls
        )