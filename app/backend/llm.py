import os

from dotenv import load_dotenv
from groq import Groq

from app.backend.prompts import (
    RAG_PROMPT,
    MCP_PROMPT,
    MULTIMODAL_PROMPT,
    SOURCE_CLASSIFIER_PROMPT,
    MCP_TOOL_PROMPT,
    PATIENT_ID_PROMPT,
    REPORT_ANALYSIS_PROMPT
)

# Load environment variables
load_dotenv()

# Get API key
GROQ_API_KEY = os.getenv(
    "GROQ_API_KEY"
)

# Initialize Groq client
client = Groq(
    api_key=GROQ_API_KEY
)

print("GROQ LOADED...")


def generate_answer(
    question,
    retrieved_chunks
):

    # Combine chunks into context
    context = "\n\n".join(
        retrieved_chunks
    )

    # Create prompt
    prompt = RAG_PROMPT.format(
    context=context,
    question=question
    )

    # Call Groq
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return answer

def determine_source(question):
    prompt = SOURCE_CLASSIFIER_PROMPT.format(
    question=question
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

    source = response.choices[0].message.content.strip()

    return source

def determine_mcp_tool(question):

    prompt = MCP_TOOL_PROMPT.format(
    question=question
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

    return response.choices[0].message.content.strip()

def extract_patient_id(question):

    prompt = PATIENT_ID_PROMPT.format(
    question=question
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

    patient_id = response.choices[0].message.content.strip()

    return int(patient_id)

def generate_mcp_answer(question, mcp_result):

    prompt = MCP_PROMPT.format(
    question=question,
    result=mcp_result
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def generate_report_analysis(report_text):

    prompt = REPORT_ANALYSIS_PROMPT.format(
    report_text=report_text
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

def generate_multimodal_answer(
    question,
    prescription_context
):

    prompt = MULTIMODAL_PROMPT.format(
    context=prescription_context,
    question=question
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content