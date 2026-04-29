from typing import TypedDict
from langgraph.graph import StateGraph, END

# 🔥 Use your existing AI function
from agents.ai_agent import extract_interaction


# 🧠 State structure
class AgentState(TypedDict):
    input_text: str
    extracted_data: dict


# 🔹 Step 1: Extract data using AI
def extract_step(state: AgentState):
    text = state["input_text"]

    ai_data = extract_interaction(text)

    return {
        "extracted_data": ai_data
    }


# 🔹 Step 2: Process / Improve data (optional logic)
def process_step(state: AgentState):
    data = state["extracted_data"]

    # Example improvement
    if data.get("sentiment") == "Positive":
        data["priority"] = "High"
    else:
        data["priority"] = "Normal"

    return {
        "extracted_data": data
    }


# 🔹 Build Graph
def build_agent():
    graph = StateGraph(AgentState)

    graph.add_node("extract", extract_step)
    graph.add_node("process", process_step)

    graph.set_entry_point("extract")

    graph.add_edge("extract", "process")
    graph.add_edge("process", END)

    return graph.compile()


# 🔥 Run agent
agent = build_agent()


def run_agent(text: str):
    result = agent.invoke({
        "input_text": text
    })

    return result["extracted_data"]