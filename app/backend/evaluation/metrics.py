"""
Evaluation metrics used by the Evaluation Agent.
"""


EVALUATION_METRICS = {

    "accuracy": {
        "description": "Measures whether the generated answer is factually correct."
    },

    "faithfulness": {
        "description": "Measures whether the answer is supported by the retrieved context."
    },

    "groundedness": {
        "description": "Measures whether the answer stays grounded in the provided context without introducing unsupported information."
    },

    "relevance": {
        "description": "Measures whether the answer addresses the user's question."
    },

    "completeness": {
        "description": "Measures whether the answer completely answers the user's question."
    },

    "hallucination": {
        "description": "Measures whether the model introduced information not present in the retrieved context."
    }

}