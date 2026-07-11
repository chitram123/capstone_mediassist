from langgraph.graph import StateGraph, END

from app.backend.graphs.state import GraphState

from app.backend.agents.planner_agent import planner_agent
from app.backend.agents.retriever_agent import retriever_agent
from app.backend.agents.mcp_agent import mcp_agent
from app.backend.agents.multimodal_agent import multimodal_agent
from app.backend.agents.reasoning_agent import reasoning_agent
from app.backend.evaluation.evaluation_agent import evaluation_agent

workflow = StateGraph(GraphState)

workflow.add_node(
    "planner",
    planner_agent
)

workflow.add_node(
    "retriever",
    retriever_agent
)

workflow.add_node(
    "mcp",
    mcp_agent
)

workflow.add_node(
    "multimodal",
    multimodal_agent
)

workflow.add_node(
    "reasoning",
    reasoning_agent
)

workflow.add_node(
    "evaluation",
    evaluation_agent
)

workflow.set_entry_point("planner")

def router(state):

    if state["source"] == "RAG":
        return "retriever"

    elif state["source"] == "MCP":
        return "mcp"

    elif state["source"] == "MULTIMODAL":
        return "multimodal"

    else:
        raise ValueError("Invalid source")
    
workflow.add_conditional_edges("planner", router)

##edges

workflow.add_edge(
    "retriever",
    "reasoning"
)

workflow.add_edge(
    "mcp",
    "reasoning"
)

workflow.add_edge(
    "multimodal",
    "reasoning"
)

workflow.add_edge(
    "reasoning",
    "evaluation"
)

workflow.add_edge(
    "evaluation",
    END
)

## Now our graph is complete
##  Final step after building graph is to initiate it using compile

graph = workflow.compile()
