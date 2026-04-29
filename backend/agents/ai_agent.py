from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import json
import re

# ✅ Latest working model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

def extract_interaction(text: str):
    prompt = f"""
Extract structured CRM interaction data from this text:

{text}

Return ONLY pure JSON. No explanation.

If any field is missing, return "Unknown"

Example:
{{
  "hcp_name": "...",
  "interaction_type": "...",
  "notes": "...",
  "sentiment": "Positive/Neutral/Negative",
  "outcome": "...",
  "follow_up": "..."
}}
"""

    try:
        response = llm.invoke(prompt)
        content = response.content

        # 🔥 Extract JSON safely
        json_match = re.search(r"\{.*\}", content, re.DOTALL)

        if json_match:
            json_str = json_match.group()

            try:
                return json.loads(json_str)
            except:
                return {"raw_output": content}
        else:
            return {"raw_output": content}

    except Exception as e:
        return {"error": str(e)}