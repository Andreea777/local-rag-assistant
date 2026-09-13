# Local RAG Assistant 

A fully local, privacy-first RAG (Retrieval-Augmented Generation) system for querying personal documents. 

## Phase 1 - Status: MVP core loop working 
- Loads PDF/TXT documents from 'data/docs/'
- Splits into overlapping chunks
- Embeds chunks with 'nomic-embed-text' via Ollama
- Stores/retrieves vectors from ChromaDB
- Generates grounded answers with 'llama3.2:3b' via Ollama
- Returns source citations alongside answers

### Challenge Faced: PDF text extraction fails on image-based/scanned pages
**Problem:** Some PDFs returned empty or no answers, while plain-text PDFs worked fine.

**Root Cause:** 'PyPDFLoader' only reads a PDF's embedded text layer. It has no OCR capability, so if a page is a scanned image or contains text baked into a picture/diagram, there is no text layer to extract, so the loader returns empty content for that page. 
This is a documented limitation of the underlaying 'pypdf' library. 

**Current scope decision:** MVP supports text-based (digital-native) PDFs and .txt files only. 

**Planned improvement:** Add an OCR fallback so scanned documents can be indexed too. 

## Stack 
Python, LangChain, Ollama, ChromaDB