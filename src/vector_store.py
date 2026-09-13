from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from src.config import CHROMA_PATH, COLLECTION_NAME, EMBEDDING_MODEL, TOP_K

def get_embedding_function(): 
    return OllamaEmbeddings(model=EMBEDDING_MODEL)

def build_vector_store(chunks):
    "Embed chunks and persist them into a local Chroma database."
    embeddings = get_embedding_function()
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_PATH,
        collection_name=COLLECTION_NAME
    )
    return vector_store

def load_vector_store():
    "Reconnect to an already-built Chroma database (no re-embedding)."
    embeddings = get_embedding_function()
    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=CHROMA_PATH
    )

def retrieve_relevant_chunks(vector_store, query, k=TOP_K):
    "Given a question, return the top-k most relevant chunks from the vector store."
    return vector_store.similarity_search(query, k=k)