import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from fastapi import APIRouter
from app.backend.graphs.graph import graph
from app.backend.rag.retriever import retrieve_chunks
from app.backend.llm import (generate_answer, determine_source,determine_mcp_tool,extract_patient_id,generate_mcp_answer,generate_multimodal_answer)
from app.backend.mcp_tool.client import execute_tool


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

    #decide the source of response
    source = determine_source(
        question
    )
    

    ###multimodal###
    if source == "MULTIMODAL":
        if not prescription_context:
            return {
            "answer": "Please upload a prescription first."
            }
        

        answer = generate_multimodal_answer(question,prescription_context)
        return {
                    "answer": answer,
                     "source": prescription_file
        }

    ###multimodal###
   
    if source == "RAG":
        retrieved_chunks = retrieve_chunks(question)
        # Create context for LLM
        context = [
        chunk["text"]
        for chunk in retrieved_chunks
        ]

        answer = generate_answer(
        question,
        context
        )
        # Get source document name
        source_document = (
        retrieved_chunks[0].get("document", "Unknown")
        if retrieved_chunks
        else "Unknown"
        )

        return {
        "answer": answer,
        "source": source_document
        }
    elif source == "MCP":
        tool = determine_mcp_tool(
            question
        )
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

        return {
        "answer": answer,
         "source": "MCP Database"
        }

    return {
        "answer": "Unable to determine source."
    }
