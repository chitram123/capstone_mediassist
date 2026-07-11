from app.backend.llm import determine_source
from app.backend.logger import logger

def planner_agent(state):

    question = state["question"]

    
    source = determine_source(question)

    logger.info("========== Planner ==========")
    logger.info(f"Question: {question}")
    logger.info(f"Selected Source: {source}")
    
    return {
        "source": source
    }