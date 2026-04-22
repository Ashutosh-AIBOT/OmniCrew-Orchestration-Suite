import os
import re
import streamlit as st
from dotenv import load_dotenv

# 1. FORCE GLOBAL NVIDIA CONFIGURATION
load_dotenv()
os.environ["OPENAI_API_BASE"] = "https://integrate.api.nvidia.com/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("NVIDIA_API_KEY")

from crewai import LLM

# Import all professional crews
from Enterprise_Content_Engine.src.blog_generation_crew.crew import BlogGenerationCrew
from Private_Knowledge_RAG.src.knowledge_crew.crew import KnowledgeCrew
from Market_Intelligence_Agent.src.news_report_crew.crew import NewsReportCrew
from Business_Audit_Summarizer.src.report_summarization_crew.crew import ReportSummarizationCrew

# Page Config
st.set_page_config(
    page_title="OmniCrew Chat Orchestrator", 
    layout="wide", 
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# RESTORED CLASSIC UI STYLING (Muted & Sleek)
st.markdown("""
    <style>
    [data-testid="collapsedControl"] { display: none; }
    .stChatMessage { border-radius: 12px; padding: 12px; margin-bottom: 8px; border: 1px solid #d1d5db; }
    .stButton>button { width: 100%; border-radius: 15px; font-weight: 500; height: 3em; }
    .stProgress > div > div > div > div { background-color: #4f46e5; }
    /* Tighten layout */
    .block-container { padding-top: 2rem; padding-bottom: 1rem; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OmniCrew Chat Orchestrator")
st.markdown("Universal Orchestration Hub | Visual Tracking v2.8.5")
st.markdown("---")

# Define Master LLM
master_llm = LLM(
    model="openai/meta/llama-3.1-8b-instruct",
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar - Permanent Control Center
with st.sidebar:
    st.title("🛡️ OmniCrew Control")
    st.status("NVIDIA Llama-3.1: ONLINE", state="complete")
    st.status("MCP Tools: DuckDuckGo, Arxiv, Serper", state="complete")
    st.status("Vector Store: LOCAL", state="complete")
    st.markdown("---")
    st.subheader("🤖 Active Specialist Units")
    st.write("✅ **Strategic Content Engine**")
    st.write("✅ **Market Intel Agent**")
    st.write("✅ **Knowledge Architects**")
    st.write("✅ **Compliance Auditors**")
    st.markdown("---")
    if st.button("🗑️ Reset All Units"):
        st.session_state.messages = []
        st.rerun()

# Intent Detection Logic - Precision Scaling
def detect_intent_with_score(text):
    text = text.lower()
    score = 0
    intent = "none"
    
    content_words = ["write", "blog", "article", "post", "whitepaper", "narrative", "author", "script", "generate", "newsletter", "documentation"]
    market_words = ["market", "competitor", "stock", "price", "revenue", "trend", "nvidia", "industry", "trading", "news", "growth", "business"]
    rag_words = ["pdf", "document", "knowledge", "analyze", "paper", "internal", "data", "study", "arxiv", "scientific", "architecture", "ai"]
    audit_words = ["audit", "compliance", "summarize", "legal", "regulatory", "report", "summary", "review", "contract", "policy"]

    c_matches = sum(1 for w in content_words if w in text)
    m_matches = sum(1 for w in market_words if w in text)
    r_matches = sum(1 for w in rag_words if w in text)
    a_matches = sum(1 for w in audit_words if w in text)

    max_matches = max(c_matches, m_matches, r_matches, a_matches)
    
    if max_matches > 0:
        if c_matches == max_matches: intent = "content_engine"
        elif m_matches == max_matches: intent = "market_intel"
        elif r_matches == max_matches: intent = "knowledge_rag"
        elif a_matches == max_matches: intent = "audit_summarizer"
        
        if max_matches == 1: score = 40
        elif max_matches == 2: score = 70
        elif max_matches >= 3: score = 100
    
    return intent, score

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Command the specialized workforce..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Logic
    with st.chat_message("assistant"):
        intent, score = detect_intent_with_score(prompt)
        
        # 1. VISUAL ROUTING ENGINE
        with st.status(f"Strategic Routing Engine...", expanded=True) as status:
            final_score = score
            if any(word in prompt.lower() for word in ["detailed", "info", "explain", "research", "deep", "study"]):
                final_score = min(final_score + 15, 100) if final_score > 0 else 0
            
            st.progress(final_score / 100, text=f"Routing Confidence: {final_score}%")
            
            if final_score >= 40:
                status.update(label=f"Specialist Verified: {intent.replace('_', ' ').upper()}", state="running")
                
                # 2. SPECIALIST EXECUTION
                try:
                    result_raw = ""
                    with st.spinner(f"Deploying {intent.replace('_', ' ').title()} Specialists..."):
                        if intent == "content_engine":
                            st.write("🛠️ **Tool Log**: Activating Strategic Content Pipeline...")
                            result = BlogGenerationCrew().crew().kickoff(inputs={'topic': prompt})
                            result_raw = result.raw
                        elif intent == "market_intel":
                            st.write("🛠️ **Tool Log**: Engaging Market Intelligence Tools...")
                            result = NewsReportCrew().crew().kickoff(inputs={'topic': prompt})
                            result_raw = result.raw
                        elif intent == "knowledge_rag":
                            st.write("🛠️ **Tool Log**: Synthesizing PDF Vector Store...")
                            result = KnowledgeCrew().crew().kickoff(inputs={'query': prompt})
                            result_raw = result.raw
                        elif intent == "audit_summarizer":
                            st.write("🛠️ **Tool Log**: Running Compliance Audit...")
                            result = ReportSummarizationCrew().crew().kickoff()
                            result_raw = result.raw
                    
                    status.update(label="Workflow Finalized", state="complete")
                    
                    # CLEAN RESPONSE OUTPUT (Same as past)
                    st.markdown("### 📊 Strategic Response")
                    st.markdown(result_raw)
                    st.session_state.messages.append({"role": "assistant", "content": result_raw})
                    
                except Exception as e:
                    status.update(label="Execution Error", state="error")
                    st.error(f"Critical System Failure: {e}")
            else:
                # 3. MASTER ORCHESTRATOR FALLBACK
                status.update(label="General Intelligence Active.", state="complete")
                try:
                    with st.spinner("Generating Professional Synthesis..."):
                        orchestrator_prompt = f"Respond professionally as an AI Orchestrator to: {prompt}"
                        response = master_llm.call([{"role": "user", "content": orchestrator_prompt}])
                        
                        st.markdown("### 🧠 Orchestrator Synthesis")
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"Reason: {e}")
