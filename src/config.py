# Models
LLM_MODEL = "llama3.2:3b"
EMBEDDING_MODEL = "nomic-embed-text"

# Paths
DOCS_PATH = "data/docs"
CHROMA_PATH = "db/chroma"
COLLECTION_NAME = "documents"

# Chunking 
CHUNK_SIZE = 500  # tokens/characters per chunk (approx)
CHUNK_OVERLAP = 50  # tokens/characters overlap between consecutive chunks 

# Retrieval
TOP_K = 4  # how many chunks to retrieve per question
