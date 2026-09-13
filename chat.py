from src.vector_store import load_vector_store, retrieve_relevant_chunks
from src.rag_pipeline import generate_answer

def main():
    print("Loading vector store...")
    vector_store = load_vector_store()
    print("Ready! Ask a question about your documents (type 'exit' or 'quit' to stop).")

    while True: 
        question = input("\nYour question: ").strip()
        if question.lower() in ["exit", "quit"]:
            print("Exiting. Goodbye!")
            break

        if not question: 
            continue  

        relevant_chunks = retrieve_relevant_chunks(vector_store, question)

        if not relevant_chunks:
            print("No relevant documents found for your question.")
            continue

        answer, sources = generate_answer(relevant_chunks, question)

        print(f"\nAnswer: {answer}")
        print(f"\nSources: {sorted(set(sources))}")

if __name__ == "__main__":
    main()