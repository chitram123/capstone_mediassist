from app.backend.llm import client
from app.backend.prompts import REASONING_PROMPT
from app.backend.logger import logger

def reasoning_agent(state):

    question = state["question"]

    answer = state["answer"]
    logger.info("========== Reason ==========")
    logger.info("Reviewing final response")

    prompt = REASONING_PROMPT.format(
    question=question,
    answer=answer
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    logger.info("Response improved")
    final_answer = response.choices[0].message.content

    logger.info("========== Completed ==========")
    logger.info("Workflow completed successfully")

    return {
        "answer": final_answer
    }