from langchain_ollama import OllamaLLM
from src.config import LLM_MODEL 

PROMPT_TEMPLATE = """Answer the question using only the context provided. 
If the answer is not contained in the context, say "I don't know based on the provided documents."

Context: 
{context}

Question: 
{question}

Answer:"""

def build_prompt(chunks, question):
    context = "\n\n---\n\n".join(chunk.page_content for chunk in chunks)
    return PROMPT_TEMPLATE.format(context=context, question=question)

def generate_answer(chunks, question):
    prompt = build_prompt(chunks, question)
    llm = OllamaLLM(model=LLM_MODEL)
    answer = llm.invoke(prompt)
    sources = [chunk.metadata.get("source", "unknown") for chunk in chunks]
    return answer, sources