import sys
import time
from pathlib import Path
from app.backend.logs.usage_logger import log_chat

sys.path.append(str(Path(__file__).resolve().parents[2]))

from fastapi import APIRouter
from app.backend.graphs.graph import graph

router = APIRouter()


@router.post("/chat")
async def chat(data: dict):

    question = data["question"]

    prescription_context = data.get(
        "prescription_context",
        ""
    )

    prescription_file = data.get(
        "prescription_file",
        "Unknown"
    )
    start_time = time.time()

    result = await graph.ainvoke(
        {
            "question": question,
            "prescription_context": prescription_context,
            "prescription_file": prescription_file,
            "tool": "",
            "mcp_result": "",
            "evaluation": "",
            "executed_agent": ""

        }
    )
    response_time = round(time.time() - start_time, 2)

    # Determine source to display in UI
    if result["source"] == "RAG":

        source = (
            result["retrieved_chunks"][0].get(
                "document",
                "Unknown"
            )
            if result.get("retrieved_chunks")
            else "Unknown"
        )

    elif result["source"] == "MULTIMODAL":

        source = prescription_file

    elif result["source"] == "MCP":

        source = "MCP Database"

    else:

        source = "Unknown"

    log_chat(
    question=question,
    source=source,
    executed_agent=result["executed_agent"],
    response_time=response_time
    )
    return {
        "answer": result["answer"],
        "source": source,
        "evaluation": result["evaluation"],
        "executed_agent": result["executed_agent"],
        "response_time": response_time
    }
