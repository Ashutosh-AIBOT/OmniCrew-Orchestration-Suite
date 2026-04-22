# HLD: CrewAI Flows Architecture

This module demonstrates advanced **Event-Driven Orchestration** using the CrewAI Flow API.

## 🏛️ Architecture Chart (Flow Patterns)

```mermaid
graph TD
    subgraph Pattern_1_Routing
        Start1[Input] --> Router{Router Node}
        Router -->|Condition A| NodeA[Success Path]
        Router -->|Condition B| NodeB[Failure Path]
    end

    subgraph Pattern_2_Parallel
        Start2[Topic] --> ParallelA[Create Notes]
        Start2[Topic] --> ParallelB[Create Q&A]
        ParallelA & ParallelB --> Merge[Compiler Agent]
    end

    subgraph Pattern_3_Stateful
        Start3[User Query] --> AgentNode[Agentic State Update]
        AgentNode -->|Update| StateObject[Shared State]
        StateObject --> FinalOutput[Final Structured Result]
    end
```

## 🛠️ Components

- **Flow API**: Manages state, triggers, and listeners.
- **Structured State**: Uses Pydantic for type-safe data sharing across nodes.
- **Orchestrator Agents**: Small, focused agents embedded within Flow nodes.
