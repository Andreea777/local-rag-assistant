import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import DOCS_PATH, CHUNK_SIZE, CHUNK_OVERLAP

def load_documents(): 
    "Load every supported file from the docs folder into LangChain Document objects."
    documents = []
    for filename in os.listdir(DOCS_PATH):
        file_path = os.path.join(DOCS_PATH, filename)

        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif filename.endswith(".txt"):
            loader = TextLoader(file_path, encoding="utf8")
        else:
            continue  # skip unsupported file types for now

        documents.extend(loader.load())

    return documents

def split_documents(documents):
    "Split loaded documents into smaller overlapping chunks."
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)