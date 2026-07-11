import asyncio
import json
import time
from pathlib import Path

import pandas as pd

from app.backend.graphs.graph import graph


# -------------------------------
# File Paths
# -------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "golden_dataset" / "rag_golden_dataset.csv"

RESULTS_DIR = BASE_DIR / "evaluation_results"
RESULTS_DIR.mkdir(exist_ok=True)

RESULT_PATH = RESULTS_DIR / "rag_evaluation_results.csv"


# -------------------------------
# Evaluation Runner
# -------------------------------

async def run_evaluation():

    dataset = pd.read_csv(DATASET_PATH)

    results = []

    print(f"\nLoaded {len(dataset)} Golden Dataset Questions\n")

    for index, row in dataset.iterrows():

        question = row["Question"]

        expected_answer = row["Expected_Answer"]

        print("=" * 70)
        print(f"Question {index + 1}")
        print(question)
        print("=" * 70)

        start = time.time()

        try:

            result = await graph.ainvoke(
                {
                    "question": question,
                    "prescription_context": "",
                    "prescription_file": "",
                    "evaluation": "",
                    "executed_agent": ""
                }
            )

            response_time = round(time.time() - start, 2)

            generated_answer = result.get(
                "answer",
                ""
            )

            evaluation = result.get(
                "evaluation",
                {}
            )

            executed_agent = result.get(
                "executed_agent",
                ""
            )

            source = result.get(
                "source",
                ""
            )

            # If evaluation is returned as JSON string,
            # convert it into dictionary.
            if isinstance(evaluation, str):

                try:

                    evaluation = json.loads(evaluation)

                except Exception:

                    evaluation = {}

            results.append(

                {

                    "ID": row["ID"],

                    "Agent": row["Agent"],

                    "Document": row["Document"],

                    "Topic": row["Topic"],

                    "Question": question,

                    "Expected_Answer": expected_answer,

                    "Generated_Answer": generated_answer,

                    "Accuracy": evaluation.get(
                        "accuracy",
                        {}
                    ).get(
                        "score",
                        ""
                    ),

                    "Faithfulness": evaluation.get(
                        "faithfulness",
                        {}
                    ).get(
                        "score",
                        ""
                    ),

                    "Groundedness": evaluation.get(
                        "groundedness",
                        {}
                    ).get(
                        "score",
                        ""
                    ),

                    "Relevance": evaluation.get(
                        "relevance",
                        {}
                    ).get(
                        "score",
                        ""
                    ),

                    "Completeness": evaluation.get(
                        "completeness",
                        {}
                    ).get(
                        "score",
                        ""
                    ),

                    "Hallucination": evaluation.get(
                        "hallucination",
                        {}
                    ).get(
                        "score",
                        ""
                    ),

                    "Overall_Score": evaluation.get(
                        "overall_score",
                        ""
                    ),

                    "Confidence": evaluation.get(
                        "confidence",
                        ""
                    ),

                    "Source": source,

                    "Executed_Agent": executed_agent,

                    "Response_Time(sec)": response_time

                }

            )

            print("**********Completed************")

        except Exception as e:

            print(f"************Failed : {e}*************")

    pd.DataFrame(results).to_csv(
        RESULT_PATH,
        index=False
    )

    print("\n")
    print("=" * 70)
    print("Evaluation Results saved to:")
    print(RESULT_PATH)


if __name__ == "__main__":

    asyncio.run(run_evaluation())