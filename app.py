import streamlit as st
from src.graph_builder import app

st.set_page_config(page_title="AI Research Paper Assistant", page_icon="📚", layout="wide")

# Title
st.title("📚 AI Research Paper Assistant (LangChain + LangGraph + Ollama)")
st.write(
    "This assistant retrieves academic papers from **ArXiv**, summarizes them into structured sections, "
    "compares findings, and generates a draft literature review — powered by **LangChain, LangGraph, and Ollama**."
)

# Input
query = st.text_input("🔎 Enter your research topic:")

# Button
if st.button("Generate Literature Review"):
    if not query.strip():
        st.warning("Please enter a research topic.")
    else:
        with st.spinner("Fetching and analyzing papers... ⏳"):
            try:
                result = app.invoke({"query": query})
                st.success("Done! ✅")
                
                # Display review
                st.subheader("📑 Generated Literature Review")
                st.write(result["literature_review"])

                # Optionally show raw steps
                with st.expander("🔬 See Agent Outputs"):
                    st.write("### Summaries")
                    for i, summary in enumerate(result.get("summaries", [])):
                        st.markdown(f"**Paper {i+1}:**\n\n{summary}\n")
                    if "comparison" in result:
                        st.write("### Comparison")
                        st.write(result["comparison"])

            except Exception as e:
                st.error(f"⚠️ Error: {e}")
