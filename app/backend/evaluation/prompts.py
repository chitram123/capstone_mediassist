"""
Prompt templates used by the Evaluation Framework.
"""

EVALUATION_PROMPT = """
You are an expert AI evaluator.

You are given:

1. User Question
2. Retrieved Context
3. Generated Answer

Your task is to evaluate the generated answer.

Evaluation Metrics:

1. Accuracy
Definition:
Is the generated answer factually correct based on the retrieved context?

2. Faithfulness
Definition:
Does the answer remain faithful to the retrieved context without changing its meaning?

3. Groundedness
Definition:
Is every important statement supported by the retrieved context?

4. Relevance
Definition:
Does the answer completely address the user's question?

5. Completeness
Definition:
Does the answer provide all important information available in the context?

6. Hallucination
Definition:
Did the model generate information that is NOT present in the retrieved context?

--------------------------------------------------

Question:
{question}

--------------------------------------------------

Retrieved Context:
{context}

--------------------------------------------------

Generated Answer:
{answer}

--------------------------------------------------

Instructions:

For EACH metric provide:

1. Score (1-10)

2. Reason (1-2 sentences)

Finally provide:

Overall Score (1-10)

Confidence Score (0-100%)

Return the response in the following JSON format ONLY.

{{
  "accuracy": {{
      "score": ...,
      "reason": "..."
  }},

  "faithfulness": {{
      "score": ...,
      "reason": "..."
  }},

  "groundedness": {{
      "score": ...,
      "reason": "..."
  }},

  "relevance": {{
      "score": ...,
      "reason": "..."
  }},

  "completeness": {{
      "score": ...,
      "reason": "..."
  }},

  "hallucination": {{
      "score": ...,
      "reason": "..."
  }},

  "overall_score": ...,

  "confidence": "..."
}}
"""