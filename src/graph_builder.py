from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.agents import summarizer_agent, comparator_agent, synthesizer_agent
from src.utils import get_docs, build_retriever

class GraphState(TypedDict, total=False):
    query: str
    papers: List[str]
    summaries: List[str]
    comparison: str
    literature_review: str

def retriever_agent(state: GraphState) -> GraphState:
    query = state["query"]
    docs = get_docs(query, max_docs=3)
    retriever = build_retriever(docs)
    results = retriever.get_relevant_documents(query)
    return {"papers": results}

def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("retriever", retriever_agent)
    graph.add_node("summarizer", summarizer_agent)
    graph.add_node("comparator", comparator_agent)
    graph.add_node("synthesizer", synthesizer_agent)

    graph.add_edge("retriever", "summarizer")
    graph.add_edge("summarizer", "comparator")
    graph.add_edge("comparator", "synthesizer")
    graph.add_edge("synthesizer", END)
    graph.set_entry_point("retriever")

    return graph.compile()

app = build_graph()
