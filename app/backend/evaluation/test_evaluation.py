from app.backend.evaluation.judge import evaluate_answer


def test_rag():

    question = "What are admission types?"

    context = """
Admission types include:

Emergency Admission
Elective Admission
Routine Admission
"""

    answer = """
The hospital supports Emergency Admission,
Elective Admission and Routine Admission.
"""

    evaluation = evaluate_answer(
        question,
        context,
        answer
    )

    print("=" * 70)
    print("RAG EVALUATION")
    print("=" * 70)
    print(evaluation)


def test_mcp():

    question = "Show lab results for patient 420"

    context = """
Patient Name: John Smith

Lab Results

Hemoglobin : 13.8
Blood Sugar : Normal
Creatinine : Normal
"""

    answer = """
Patient John Smith's laboratory results are:

• Hemoglobin : 13.8

• Blood Sugar : Normal

• Creatinine : Normal
"""

    evaluation = evaluate_answer(
        question,
        context,
        answer
    )

    print("\n")
    print("=" * 70)
    print("MCP EVALUATION")
    print("=" * 70)
    print(evaluation)


def test_multimodal():

    question = "What medicines are prescribed?"

    context = """
Patient Name : John Smith

Medicine

Paracetamol 650 mg

Take one tablet twice daily after food.

Vitamin C

Once daily after breakfast.
"""

    answer = """
Medicines prescribed:

• Paracetamol 650 mg

• Vitamin C

Take one tablet twice daily after food.
"""

    evaluation = evaluate_answer(
        question,
        context,
        answer
    )

    print("\n")
    print("=" * 70)
    print("MULTIMODAL EVALUATION")
    print("=" * 70)
    print(evaluation)


if __name__ == "__main__":

    test_rag()

    test_mcp()

    test_multimodal()