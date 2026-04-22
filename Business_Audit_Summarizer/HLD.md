# HLD: Report Summarization Crew

This crew uses a **Sequential Process** with **Guardrails** to ensure summaries meet specific length requirements.

## 🏛️ Architecture Chart

```mermaid
graph TD
    User[Full Report] --> GenAgent[Report Generator Agent]
    GenAgent --> Draft[Raw Report Draft]
    
    subgraph Refinement_Loop
        Draft --> SumAgent[Report Summarizer Agent]
        SumAgent --> Summary[Summary Output]
        Summary --> Guard[Guardrail: Word Count < 400]
        Guard -->|Fail| SumAgent
        Guard -->|Pass| Final[report_summary_new.md]
    end
```

## 🛠️ Components
- **Report Generator**: Drafts the initial full report.
- **Report Summarizer**: Compresses the report into a summary.
- **Guardrail**: A Python function that validates word count and triggers retries if necessary.
- **LLM**: Powered by NVIDIA NIM (Llama-3.1-70B).
