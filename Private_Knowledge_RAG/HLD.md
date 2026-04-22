# HLD: Knowledge Crew

This crew demonstrates **Retrieval Augmented Generation (RAG)** by integrating local PDF documents into the agent's knowledge base.

## 🏛️ Architecture Chart

```mermaid
graph TD
    PDF[PDF Source: survey_on_icl.pdf] --> VectorStore[CrewAI Knowledge Source]
    User[Summarization Request] --> Agent[Research Summarization Agent]
    
    subgraph RAG_Process
        Agent -->|Query| VectorStore
        VectorStore -->|Context| Agent
        Agent -->|Analyze| Result[Summarized Knowledge]
    end
    
    Result --> Output[Terminal/Output]
```

## 🛠️ Components
- **PDFKnowledgeSource**: Handles chunking and embedding of the PDF.
- **Research Summarization Agent**: Specialized in analyzing long technical documents.
- **LLM**: Powered by NVIDIA NIM (Llama-3.1-70B).
