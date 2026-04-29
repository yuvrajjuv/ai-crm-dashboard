from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
import os

def simple_tag(notes: str):
    notes = notes.lower()

    if "price" in notes or "cost" in notes:
        return "💰 Pricing Discussion"
    elif "follow" in notes:
        return "📞 Follow-up"
    elif "interested" in notes:
        return "🔥 Interested"
    else:
        return "📝 General"


def generate_tag(notes: str):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return simple_tag(notes)

        llm = ChatOpenAI(api_key=api_key)

        response = llm.invoke([
            HumanMessage(content=f"Give one short CRM tag for: {notes}")
        ])

        return response.content

    except:
        return simple_tag(notes)