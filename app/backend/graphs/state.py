from typing import TypedDict


class GraphState(TypedDict):

    question: str

    source: str

    answer: str

    retrieved_chunks: list

    prescription_context: str

    prescription_file: str

    tool: str

    mcp_result: str

    evaluation: str

    executed_agent: str