from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import ArxivLoader
from langchain.vectorstores import Chroma
from src.config import MODEL_EMBEDDING, VECTORSTORE_DIR

embeddings = OllamaEmbeddings(model=MODEL_EMBEDDING)

def get_docs(query, max_docs=3):
    loader = ArxivLoader(query=query, max_docs=max_docs)
    return loader.load()

def build_retriever(docs):
    db = Chroma.from_documents(docs, embeddings, persist_directory=VECTORSTORE_DIR)
    return db.as_retriever(search_kwargs={"k": 3})
