# HLD: Guide Generator Flow

This is a **Multi-Crew Orchestration** system that connects a research team and a writing team.

## 🏛️ Architecture Chart

```mermaid
graph TD
    User[Source Links] --> Flow[GuideGeneratorFlow]
    
    subgraph Crew_1_Research ["🔍 Research Crew (Hierarchical)"]
        Flow --> ResManager[Research Manager]
        ResManager --> YT[YouTube Specialist]
        ResManager --> Web[Web Specialist]
        ResManager --> Arxiv[arXiv Specialist]
        ResManager --> Docs[Doc Specialist]
        YT & Web & Arxiv & Docs --> ResReport[Research Report]
    end
    
    ResReport --> Flow
    
    subgraph Crew_2_Writing ["✍️ Writing Crew (Sequential)"]
        Flow --> Writer[Technical Writer]
        Writer --> Editor[Content Editor]
        Editor --> FinalGuide[getting_started_guide.md]
    end
```

## 🛠️ Components
- **Research Crew**: A hierarchical unit focused on data gathering.
- **Writing Crew**: A sequential unit focused on content polish.
- **Shared State**: Passes the research report from the first crew to the second.
- **LLM**: Powered by NVIDIA NIM (Llama-3.1-70B).
