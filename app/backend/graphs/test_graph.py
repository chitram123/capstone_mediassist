import asyncio

from app.backend.graphs.graph import graph


async def main():

    result = await graph.ainvoke(
        {
            "question": "What medicines are prescribed?",
            "prescription_context": """
Patient Name: John Smith

Medicine:
Paracetamol 650 mg
Take one tablet twice daily after food.

Vitamin C
Once daily after breakfast.
""",
            "prescription_file": "prescription.jpg"
        }
    )

    print(result)


asyncio.run(main())