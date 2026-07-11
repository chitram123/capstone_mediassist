import asyncio

from fastmcp.client import Client
from fastmcp.client import PythonStdioTransport

from pathlib import Path

from pathlib import Path

server_path = Path(__file__).resolve().parent / "server.py"

project_root = Path(__file__).resolve().parents[3]

transport = PythonStdioTransport(
    script_path=str(server_path),
    cwd=str(project_root)
)

client = Client(transport)


async def execute_tool(
    tool_name: str,
    params: dict
):
    async with client:

        result = await client.call_tool(
            tool_name,
            params
        )

        if result.content:
            return result.content[0].text

        return "No records found"

if __name__ == "__main__":

    result = asyncio.run(
        execute_tool(
            "lab_results",
            {
                "patient_id": 4999
            }
        )
    )

    print(result)