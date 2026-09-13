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

        loaded = loader.load()
        # warn if a file produced (almost) no detectable text -> strong signal if the file is not actually text-based (e.g., scanned images)
        total_chars = sum(len(doc.page_content) for doc in loaded)
        if total_chars < 20: 
            print(f"Warning: {filename} contains very little detectable text - it may be a scanned or image-based pdf.")

        documents.extend(loaded)

    return documents

def split_documents(documents):
    "Split loaded documents into smaller overlapping chunks."
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return text_splitter.split_documents(documents)