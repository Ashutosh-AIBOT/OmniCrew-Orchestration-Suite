import os
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.knowledge.source.pdf_knowledge_source import PDFKnowledgeSource
from typing import List

# Load environment variables
load_dotenv()

# Define the High-Speed NVIDIA LLM
nvidia_llm = LLM(
    model="openai/meta/llama-3.1-8b-instruct",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# define the pdf knowledge source with LOCAL EMBEDDINGS
# This prevents the 401 OpenAI error during document "upsert"
research_paper_source = PDFKnowledgeSource(
    file_paths=["survey_on_icl.pdf"],
    chunk_size=1500,
    chunk_overlap=250,
    embedder={
        "provider": "huggingface",
        "config": {
            "model": "sentence-transformers/all-MiniLM-L6-v2"
        }
    }
)

@CrewBase
class KnowledgeCrew():
    """KnowledgeCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # define the path for config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # define our agent
    @agent
    def research_summarization(self) -> Agent:
        return Agent(
            config=self.agents_config["research_summarization"],
            verbose=True,
            llm=nvidia_llm
        )
        
    # define the task
    @task
    def summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config["summarization_task"]
        )
        
    # define the crew
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            knowledge_sources=[research_paper_source],
            memory=False, # Disabled to ensure total NVIDIA/Local independence
            planning=False
        )