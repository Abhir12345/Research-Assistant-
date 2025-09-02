# 📚 AI Research Paper Assistant (LangChain + LangGraph + Ollama)

A local, privacy-preserving **AI research assistant** that:
- Retrieves academic papers from **ArXiv**.
- Summarizes them into structured sections (Background, Methods, Results, Conclusion).
- Compares multiple papers and highlights similarities/differences.
- Generates a mini **literature review draft**.

Built with **LangChain**, **LangGraph**, and **Ollama** (Gemma + nomic-embed-text).

---

## 🚀 Features
- **Retrieval-Augmented Generation (RAG):** Store and retrieve papers in a persistent vectorstore (Chroma).
- **Multi-Agent Orchestration:** LangGraph pipeline with retriever, summarizer, comparator, and synthesizer agents.
- **Local-Only:** Runs completely offline using Ollama models (no OpenAI API).
- **User Interfaces:** 
  - CLI (`main.py`) 
  - Streamlit app (`app.py`) for interactive demo.

---

## ⚙️ Tech Stack
- **LLM:** [Ollama](https://ollama.ai/) (`mistral`, `phi3`, `nomic-embed-text`)
- **Frameworks:** LangChain, LangGraph
- **Vector Store:** Chroma
- **UI:** Streamlit

---

## 📦 Installation
```bash
git clone https://github.com/Abhir12345/Research-Assistant.git
cd Research-Assistant
pip install -r requirements.txt
