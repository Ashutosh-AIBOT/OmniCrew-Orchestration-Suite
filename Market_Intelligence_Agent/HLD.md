# HLD: News Report Crew

This crew specializes in gathering web news and outputting data in a **Structured JSON** format.

## 🏛️ Architecture Chart

```mermaid
graph TD
    User[Topic] --> Agent[News Reporter Agent]
    Agent -->|Search| Web[Serper.dev Web Search]
    Web -->|Raw Data| Agent
    
    subgraph Data_Structuring
        Agent -->|Parse| Pydantic[NewsReport Pydantic Model]
        Pydantic -->|Schema Validation| FinalJSON[news.json]
    end
    
    FinalJSON --> End[System/API Consumption]
```

## 🛠️ Components
- **News Reporter Agent**: Uses `SerperDevTool` for real-time news.
- **Pydantic Model**: Defines the structure (Headline, URL, Summary, Agency).
- **LLM**: Powered by NVIDIA NIM (Llama-3.1-70B).
