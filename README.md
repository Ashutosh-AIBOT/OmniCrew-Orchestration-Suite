# 🛡️ OmniCrew Orchestration Suite

A production-grade, multi-agent enterprise platform powered by **NVIDIA NIM** and **CrewAI**. This suite orchestrates 18+ specialized agents across 5 strategic business units to deliver high-fidelity automation.

## 🌟 The OmniCrew Vision
This project transforms basic AI scripts into a unified **Agentic Operating System**. It features a conversational "Command Center" that intelligently routes tasks to specialized agent teams based on user intent.

## 🏢 Business Units (The Workforce)
1.  **Enterprise Content Engine**: High-impact B2B content and whitepapers.
2.  **Market Intelligence Agent**: Real-time competitor and trend tracking.
3.  **Private Knowledge RAG**: Secure intelligence extraction from your PDFs.
4.  **Business Audit Summarizer**: Compliance-heavy document auditing.
5.  **Master Workflow Orchestrator**: Complex multi-crew event-driven flows.

## 🛠️ Technical Innovations
- **Global NVIDIA NIM Integration**: Powered by Llama-3.1-8B for elite speed.
- **Local Embedding Architecture**: Uses HuggingFace locally for PDF analysis (Zero OpenAI dependence).
- **Conversational Orchestrator**: An `app.py` interface with Regex-based intent detection.
- **Enterprise Observability**: Integrated LangSmith tracing for full system auditability.

## 🚀 Deployment & Usage
- **Chat Hub (Recommended)**: `streamlit run app.py`
- **Admin Dashboard**: `streamlit run dashboard.py`
- **Developer API**: `uvicorn fastapi_app:app --reload`

## 🙏 Credits
Inspired by the multi-agent foundations of **CampusX**, evolved into a professional enterprise-grade suite by **Ashutosh**.
