import os
from dotenv import load_dotenv

# 1. FORCE GLOBAL NVIDIA CONFIGURATION BEFORE ANY IMPORTS
load_dotenv()
os.environ["OPENAI_API_BASE"] = "https://integrate.api.nvidia.com/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("NVIDIA_API_KEY")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Import all professional crews
from Enterprise_Content_Engine.src.blog_generation_crew.crew import BlogGenerationCrew
from Private_Knowledge_RAG.src.knowledge_crew.crew import KnowledgeCrew
from Market_Intelligence_Agent.src.news_report_crew.crew import NewsReportCrew
from Business_Audit_Summarizer.src.report_summarization_crew.crew import ReportSummarizationCrew

app = FastAPI(
    title="Ashutosh OmniCrew Orchestration Suite API",
    description="Unified API for Strategic Content, Market Intelligence, and Private RAG.",
    version="1.0.0"
)

class AgentRequest(BaseModel):
    topic: str

@app.post("/content/generate")
async def run_content_engine(request: AgentRequest):
    """Generates strategic B2B content."""
    try:
        result = BlogGenerationCrew().crew().kickoff(inputs={'topic': request.topic})
        return {"status": "success", "output": result.raw}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/market/intelligence")
async def run_market_intel(request: AgentRequest):
    """Extracts market intelligence and competitor data."""
    try:
        result = NewsReportCrew().crew().kickoff(inputs={'topic': request.topic})
        return {"status": "success", "output": result.raw}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/knowledge/query")
async def run_rag_query(request: AgentRequest):
    """Queries private PDF knowledge base."""
    try:
        result = KnowledgeCrew().crew().kickoff(inputs={'topic': request.topic})
        return {"status": "success", "output": result.raw}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "online", "engine": "NVIDIA NIM Llama-3.1-70B"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
