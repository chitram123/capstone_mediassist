from app.backend.llm import generate_multimodal_answer
from app.backend.logger import logger

def multimodal_agent(state):

    question = state["question"]

    prescription_context = state["prescription_context"]

    answer = generate_multimodal_answer(
        question,
        prescription_context
    )

    logger.info("========== Multimodal ==========")
    logger.info("Prescription context received")
    logger.info("Generated multimodal response")

    return {
        "answer": answer
    }