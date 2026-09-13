from src.ingest import load_documents, split_documents
from src.vector_store import build_vector_store
from src.rag_pipeline import generate_answer

def main():
    print("Loading documents...")
    documents = load_documents()
    print(f"Loaded {len(documents)} document(s).")

    print("Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} chunk(s).")

    print("Building vector store (embedding chunks)...")
    vector_store = build_vector_store(chunks)
    print("Vector store ready.")

    # hardcoded test question 
    question = "What do the Alps and the Pyrenees provide?"

    print(f"\nQuestion: {question}")
    relevant_chunks = vector_store.similarity_search(question, k=4)

    answer, sources = generate_answer(relevant_chunks, question)

    print(f"\nAnswer: {answer}")
    print(f"\nSources: {set(sources)}")

if __name__ == "__main__":
    main()