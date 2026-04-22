# 📓 OmniCrew Technical Notes & Implementation Details

This document provides granular technical details for developers and stakeholders interested in the internal mechanics of the **OmniCrew Orchestration Suite**.

## 🚀 Core Engine Specifications
- **Framework**: CrewAI 0.100.1
- **Primary LLM**: NVIDIA NIM `meta/llama-3.1-8b-instruct`
- **Embedding Model**: Local HuggingFace `all-MiniLM-L6-v2`
- **Frontend**: Streamlit 1.32.0+
- **Backend API**: FastAPI 0.109.0+

## 🧠 Strategic Decision Log

### 1. Why NVIDIA NIM instead of OpenAI?
- **Cost-Efficiency**: High-throughput tokens at a fraction of the cost.
- **Speed**: Optimized GPU kernels for Llama-3.1-8B provide near-instant responses.
- **Independence**: Reduces vendor lock-in with OpenAI.

### 2. Why Local Embeddings?
- **Privacy**: Your business documents (PDFs) are processed on your local machine. No document data is sent to a third-party embedding server.
- **401 Prevention**: Eliminates the "Incorrect API Key" errors often associated with vector store upserts.

### 3. Regex Intent Detection
- **Mechanism**: The `detect_intent` function in `app.py` uses multi-pattern regex to classify natural language queries.
- **Benefit**: Zero cost for routing. Most "Chat" systems waste an LLM call just to decide which tool to use. OmniCrew does this for free.

## 🛠️ Environment Configuration
| Variable | Purpose | Required |
| :--- | :--- | :--- |
| `NVIDIA_API_KEY` | Powers the reasoning agents | Yes |
| `SERPER_API_KEY` | Powers the web research tools | Yes |
| `LANGCHAIN_API_KEY`| Powers observability/tracing | Optional |

## 📦 Deployment Guardrails
- **Memory Management**: Memory is currently disabled (`memory=False`) to ensure maximum compatibility with the local embedding layer.
- **Planning**: Disabled (`planning=False`) to bypass OpenAI-specific beta endpoints not supported by current NIM servers.

---
*Maintained by Ashutosh | Strategic AI Engineering*
