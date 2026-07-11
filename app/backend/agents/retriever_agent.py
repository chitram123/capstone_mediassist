from app.backend.rag.retriever import retrieve_chunks
from app.backend.llm import generate_answer
from app.backend.logger import logger

def retriever_agent(state):

    question = state["question"]

    retrieved_chunks = retrieve_chunks(question)


    context = [
        chunk["text"]
        for chunk in retrieved_chunks
    ]

    answer = generate_answer(
        question,
        context
    )
    logger.info("========== RAG ==========")
    logger.info(f"Retrieved {len(retrieved_chunks)} chunks")
    logger.info("Generated RAG response")
    
    return {
        "retrieved_chunks": retrieved_chunks,
        "answer": answer
    }