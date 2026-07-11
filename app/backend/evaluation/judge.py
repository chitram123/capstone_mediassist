from app.backend.llm import client

from app.backend.evaluation.prompts import (
    EVALUATION_PROMPT
)


def evaluate_answer(
    question,
    context,
    answer
):

    prompt = EVALUATION_PROMPT.format(
        question=question,
        context=context,
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

    evaluation = response.choices[0].message.content

    return evaluation