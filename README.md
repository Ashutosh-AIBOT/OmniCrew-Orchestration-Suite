---
title: OmniCrew Enterprise Hub
emoji: 🛡️
colorFrom: indigo
colorTo: gray
sdk: docker
app_file: app.py
pinned: false
---

# 🛡️ OmniCrew Orchestration Suite
### Universal Multi-Agent Enterprise Platform | NVIDIA NIM Powered

A production-grade, multi-agent enterprise platform powered by **NVIDIA NIM** and **CrewAI**. This suite orchestrates specialized agents across strategic business units to deliver high-fidelity automation.

## 🚀 Specialist Units
*   ✍️ **Content Engine**: High-impact B2B content and whitepapers.
*   🔍 **Market Intel**: Real-time competitor and trend tracking.
*   📚 **Knowledge Architects**: Secure intelligence extraction from your PDFs.
*   📋 **Audit Summarizer**: Compliance-heavy document auditing.

## 🧠 Technical Innovations
- **Global NVIDIA NIM Integration**: Powered by Llama-3.1-8B for elite speed.
- **Local Embedding Architecture**: Uses HuggingFace locally for PDF analysis (Zero OpenAI dependence).
- **Conversational Orchestrator**: An `app.py` interface with Regex-based intent detection.
- **Enterprise Observability**: Integrated LangSmith tracing for full system auditability.

## 🛠️ Configuration
This app requires the following secrets to be set in the Space settings:
- `NVIDIA_API_KEY`: For LLM reasoning.
- `LANGCHAIN_API_KEY`: (Optional) For observability.

## 🚀 Deployment & Usage
- **Chat Hub (Recommended)**: `streamlit run app.py`
- **Admin Dashboard**: `streamlit run dashboard.py`
- **Developer API**: `uvicorn fastapi_app:app --reload`

---
*Developed for Strategic AI Excellence | 2026*
