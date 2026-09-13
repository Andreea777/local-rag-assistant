# Local RAG Assistant 

A fully local, privacy-first RAG (Retrieval-Augmented Generation) system for querying personal documents. 

## Phase 1 - Status: MVP core loop working 
- Loads PDF/TXT documents from 'data/docs/'
- Splits into overlapping chunks
- Embeds chunks with 'nomic-embed-text' via Ollama
- Stores/retrieves vectors from ChromaDB
- Generates grounded answers with 'llama3.2:3b' via Ollama
- Returns source citations alongside answers

## Stack 
Python, LangChain, Ollama, ChromaDB