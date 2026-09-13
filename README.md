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

## Phase 2 - Status: Multi-document indexing + interactive terminal chat
- Indexing and querying are now separate steps 
- Supports multiple documents in 'data/docs/' simultaneously 
- Interactive chat loop - ask multiple questions per session 
- Source citations now include page numbers
- Added a warning for documents that produce little/ no extractable text 

### Retrieval is sensitive to spelling/typos
**Observation:** Questions with typos sometimes fail to retrieve relevant chunks, even when a correctly spelled version works.

**Root Cause:** Embedding models tokenize text into sub-word units before vectorizing. Misspelled words often tokenize very differently from their correct form, shifting the result vector away from the semantically correct region of embedding space.

**Planned improvement:** Add hybrid search (dense embeddings + BM25 keyword matching) so exact/near-exact term matches are not lost when semantic similarity drifts. 

## Stack 
Python, LangChain, Ollama, ChromaDB