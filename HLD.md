# 🏛️ OmniCrew Master Architecture (HLD)

This High-Level Design document outlines the complete architectural orchestration of the **OmniCrew Orchestration Suite**, featuring a **High-Confidence Intent Routing Layer**.

## 📊 Detailed System Orchestration Chart

```mermaid
graph TD
    %% Global Entry Points
    User((<b>End User</b>)) -->|Input Query| ChatUI[<b>Streamlit Chat Hub</b><br/>app.py]
    
    %% Intelligence Layer (The Regex Engine)
    subgraph Cognitive_Routing ["🧠 Intent Orchestration (60% Threshold)"]
        ChatUI --> PatternScan[Regex Pattern Scanner]
        PatternScan --> ScoreCalc[Confidence Score Calculator]
        
        ScoreCalc --> Decision{<b>Score >= 60%?</b>}
        
        Decision -->|No: Low Signal| GenAI[General Assistant Mode]
        Decision -->|Yes: High Signal| Router[Master Specialist Router]
    end

    %% UI Feedback Layer
    subgraph UI_Feedback ["🖥️ Real-time Status Monitoring"]
        ScoreCalc -->|Visual Feedback| ProgressBar[Streamlit Progress Bar]
        Router -->|Visual Feedback| StatusLog[st.status: Specialist Logs]
    end

    %% The Specialists (Business Units)
    subgraph Agent_Workforce ["🤝 Specialized Agent Crews"]
        Router --> BU1[<b>Enterprise Content Engine</b><br/>Team: Strategic Comm Directors]
        Router --> BU2[<b>Market Intelligence Agent</b><br/>Team: Lead Intel Analysts]
        Router --> BU3[<b>Private Knowledge RAG</b><br/>Team: Knowledge Architects]
        Router --> BU4[<b>Business Audit Summarizer</b><br/>Team: Compliance Auditors]
    end

    %% Execution Layer
    subgraph Model_Data_Layer ["🏗️ Model & Data Services"]
        BU1 & BU2 & BU3 & BU4 & GenAI --> LLM[<b>NVIDIA NIM</b><br/>Llama-3.1-8B-Instruct]
        BU2 --> WebSearch[<b>Serper.dev</b><br/>Real-Time News Engine]
        BU3 --> Embedder[<b>Local Embeddings</b><br/>HF all-MiniLM-L6-v2]
        LLM -.-> Tracing[<b>LangSmith</b><br/>Strategic Observability]
    end

    %% Outputs
    BU1 & BU2 & BU3 & BU4 --> FinalDocs{Final Deliverables}
    FinalDocs --> Markdown[Professional Markdown]
    FinalDocs --> UIFeed[Interactive UI Results]
```

## 🧩 Architectural Deep-Dive

### 1. High-Confidence Cognitive Routing
The core innovation of OmniCrew is the **60% Confidence Gate**. Unlike traditional systems that guess user intent, OmniCrew uses a multi-pattern Regex scanner. A specialized "Specialist Crew" is only activated if **2 or more** high-signal keywords are detected (Total Score >= 60%).

### 2. Live Orchestration Monitoring (UI)
The architecture includes a real-time feedback loop. Users see exactly what the system is "thinking":
- **Confidence Meter**: Shows the mathematical certainty of the intent detection.
- **Workflow Status**: Expands to show live logs of which specialist is active and which tool (Search, Vector DB) is being called.

### 3. Model & Data Hybridization
- **LLM**: Centralized reasoning via **NVIDIA NIM** for high-speed inference.
- **RAG**: Local document processing via **HuggingFace** to ensure 100% data privacy and 0% OpenAI API dependence.

---
*Architected for Enterprise Stability, Security, and Scalable Performance.*
