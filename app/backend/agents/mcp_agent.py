from app.backend.llm import (
    determine_mcp_tool,
    extract_patient_id,
    generate_mcp_answer
)

from app.backend.mcp_tool.client import execute_tool
from app.backend.logger import logger


async def mcp_agent(state):

    question = state["question"]
    
    tool = determine_mcp_tool(question)
    
    # --------------------------
    # Search Patient
    # --------------------------

    if tool == "search_patient":

        patient_name = question.lower().replace(
            "search patient",
            ""
        ).strip()

        if not patient_name:

            return {
                "answer": "Please provide a patient name. For example: Search patient John Smith."
            }

        result = await execute_tool(
            tool,
            {
                "patient_name": patient_name
            }
        )

    # --------------------------
    # Other MCP Tools
    # --------------------------

    else:

        patient_id = extract_patient_id(question)

        if tool == "lab_results" and patient_id is None:

            return {
                "answer": "Please provide a patient ID to retrieve lab results."
            }

        elif tool == "patient_history" and patient_id is None:

            return {
                "answer": "Please provide a patient ID to retrieve patient history."
            }

        elif tool == "payment_summary" and patient_id is None:

            return {
                "answer": "Please provide a patient ID to retrieve billing information."
            }

        result = await execute_tool(
            tool,
            {
                "patient_id": patient_id
            }
        )

    answer = generate_mcp_answer(
        question,
        result
    )
    logger.info("========== MCP ==========")
    logger.info(f"Selected Tool: {tool}")
    logger.info("Tool execution completed")
    return {
        "tool": tool,
        "mcp_result": result,
        "answer": answer
    }