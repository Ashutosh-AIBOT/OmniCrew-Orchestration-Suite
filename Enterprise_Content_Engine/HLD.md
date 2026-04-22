# HLD: Blog Generation Crew

This crew uses a **Hierarchical Process** to research, write, and review blog content.

## 🏛️ Architecture Chart

```mermaid
graph TD
    User[Topic Input] --> Manager[Team Leader Agent]
    
    subgraph Crew_Collaboration
        Manager --> Researcher[Expert Researcher]
        Researcher --> ResearchReport[Research Report]
        ResearchReport --> Manager
        
        Manager --> Writer[Expert Blog Writer]
        Writer --> BlogDraft[Blog Draft]
        BlogDraft --> Manager
        
        Manager --> Reviewer[Expert Blog Reviewer]
        Reviewer --> Feedback[Feedback & Polish]
        Feedback --> Manager
    end
    
    Manager --> FinalOutput[blog.md]
```

## 🛠️ Components
- **Manager (Team Leader)**: Orchestrates the workflow and delegates tasks.
- **Researcher**: Uses `SerperDevTool` for web research.
- **Writer**: Focuses on engaging tone and analogies.
- **Reviewer**: Ensures quality and simplicity.
- **LLM**: Powered by NVIDIA NIM (Llama-3.1-70B).
