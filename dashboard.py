import os
from dotenv import load_dotenv

# 1. FORCE GLOBAL NVIDIA CONFIGURATION
load_dotenv()
os.environ["OPENAI_API_BASE"] = "https://integrate.api.nvidia.com/v1"
os.environ["OPENAI_API_KEY"] = os.getenv("NVIDIA_API_KEY")

import streamlit as st

# Import all professional crews
from Enterprise_Content_Engine.src.blog_generation_crew.crew import BlogGenerationCrew
from Private_Knowledge_RAG.src.knowledge_crew.crew import KnowledgeCrew
from Market_Intelligence_Agent.src.news_report_crew.crew import NewsReportCrew
from Business_Audit_Summarizer.src.report_summarization_crew.crew import ReportSummarizationCrew

# Page Config
st.set_page_config(page_title="OmniCrew Admin Dashboard", layout="wide", page_icon="🛡️")

# Professional UI Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: #ffffff; border-radius: 10px 10px 0 0; gap: 1px; padding-top: 10px; }
    .stTabs [aria-selected="true"] { background-color: #f0f2f6; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ OmniCrew Admin Dashboard")
st.markdown("Enterprise Multi-Agent Control Center | NVIDIA NIM Powered")
st.markdown("---")

# Create 4 Tabs for the Specialist Units
tab1, tab2, tab3, tab4 = st.tabs([
    "✍️ Content Engine", 
    "🔍 Market Intel", 
    "📚 Knowledge RAG", 
    "📋 Audit Summarizer"
])

# --- TAB 1: Enterprise Content Engine ---
with tab1:
    st.subheader("✍️ Strategic Content Generation")
    st.info("Agents: Strategic Director, Content Analyst, Executive Strategist, Compliance Editor")
    topic = st.text_input("Enter Topic for Whitepaper:", placeholder="e.g., The Future of Generative AI in B2B")
    
    if st.button("🚀 Launch Content Crew"):
        if topic:
            with st.status("Orchestrating Content Team...", expanded=True):
                result = BlogGenerationCrew().crew().kickoff(inputs={'topic': topic})
                st.markdown(result.raw)
        else:
            st.warning("Please enter a topic.")

# --- TAB 2: Market Intelligence Agent ---
with tab2:
    st.subheader("🔍 Market Intelligence Extraction")
    st.info("Agents: Lead Market Intelligence Analyst | Tool: Serper.dev Real-Time Search")
    m_topic = st.text_input("Enter Market to Track:", placeholder="e.g., NVIDIA Blackwell Demand")
    
    if st.button("🚀 Launch Intel Crew"):
        if m_topic:
            with st.status("Scanning Global News Channels...", expanded=True):
                result = NewsReportCrew().crew().kickoff(inputs={'topic': m_topic})
                st.markdown(result.raw)
        else:
            st.warning("Please enter a market topic.")

# --- TAB 3: Private Knowledge RAG ---
with tab3:
    st.subheader("📚 Private Knowledge Intelligence")
    st.info("Agents: Principal Knowledge Architect | Tool: Local HF-Embeddings")
    
    uploaded_file = st.file_uploader("📂 Upload Business Document (PDF)", type="pdf")
    if uploaded_file:
        # Save file to knowledge directory
        knowledge_dir = "knowledge"
        if not os.path.exists(knowledge_dir):
            os.makedirs(knowledge_dir)
        
        file_path = os.path.join(knowledge_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Document '{uploaded_file.name}' indexed successfully.")

    k_query = st.text_input("Enter Query for Document:", placeholder="e.g., What are the key risks mentioned?")
    
    if st.button("🚀 Launch Knowledge Crew"):
        if k_query:
            with st.status("Analyzing Internal Knowledge Base...", expanded=True):
                result = KnowledgeCrew().crew().kickoff(inputs={'query': k_query})
                st.markdown(result.raw)
        else:
            st.warning("Please enter a query.")

# --- TAB 4: Business Audit Summarizer ---
with tab4:
    st.subheader("📋 Executive Audit Summarization")
    st.info("Agents: Strategic Compliance Auditor, Executive Summary Specialist")
    
    if st.button("🚀 Launch Audit Crew"):
        with st.status("Synthesizing Business Audit...", expanded=True):
            result = ReportSummarizationCrew().crew().kickoff()
            st.markdown(result.raw)

# Sidebar - System Health
with st.sidebar:
    st.title("🛡️ System Health")
    st.write("● LLM Engine: **Llama-3.1-8B**")
    st.write("● Reasoning: **Specialized**")
    st.write("● Process: **Sequential**")
    st.markdown("---")
    st.caption("Strategic AI Architecture | 2026")
