# run 'python index_documents.py' to index your documents for retrieval, everytime you add new documents to the 'data/docs' folder.

from src.ingest import load_documents, split_documents
from src.vector_store import build_vector_store

def main():
    print("Loading documents...")
    documents = load_documents()

    if not documents:
        print("No documents found in the specified directory. Add some .pdf or .txt files first.")
        return 

    print(f"Loaded {len(documents)} document page(s)/file(s).")

    print("Splitting into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunk(s).")

    print("Embedding chunks and building vector store...")
    build_vector_store(chunks)
    print("Indexing complete! You can now run chat.py to ask questions about your documents.")

if __name__ == "__main__":
    main()
