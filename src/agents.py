from langchain_community.llms import Ollama
from src.config import MODEL_LLM

llm = Ollama(model=MODEL_LLM)

def summarizer_agent(state):
    summaries = []
    for doc in state["papers"]:
        prompt = f"Summarize this paper in 4 sections: Background, Methods, Results, Conclusion.\n\n{doc.page_content[:2000]}"
        summary = llm.invoke(prompt)
        summaries.append(summary)
    return {"summaries": summaries}

def comparator_agent(state):
    prompt = f"Compare these research summaries and highlight similarities & differences:\n\n{state['summaries']}"
    comparison = llm.invoke(prompt)
    return {"comparison": comparison}

def synthesizer_agent(state):
    prompt = f"Write a short literature review draft based on the following comparison:\n\n{state['comparison']}"
    lit_review = llm.invoke(prompt)
    return {"literature_review": lit_review}
