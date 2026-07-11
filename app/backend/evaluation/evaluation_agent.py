from app.backend.evaluation.judge import evaluate_answer

from app.backend.logger import logger


def evaluation_agent(state):

    logger.info("========== Evaluation ==========")

    question = state["question"]

    answer = state["answer"]

    retrieved_chunks = state.get(
    "retrieved_chunks",
    []
    )

    if retrieved_chunks:
        context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
        )

    elif state["source"] == "MULTIMODAL":
        context = state.get(
        "prescription_context",
        ""
        )

    elif state["source"] == "MCP":
        context = state.get(
        "mcp_result",
        ""
        )

    else:
        context = ""

    source = state.get(
        "source",
        "Unknown"
    )

    evaluation = evaluate_answer(
        question=question,
        context=context,
        answer=answer
    )

    logger.info("Evaluation Completed")

    return {

        "evaluation": evaluation,

        "executed_agent": source

    }