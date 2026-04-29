from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import get_db
from models.interaction import Interaction
from agents.langgraph_agent import run_agent

router = APIRouter()


# 🔹 Request Schema
from pydantic import BaseModel


class AIRequest(BaseModel):
    text: str


# 🔥 AI + DB SAVE
@router.post("/ai-agent")
def ai_agent(request: AIRequest, db: Session = Depends(get_db)):
    
    # 1️⃣ Run AI Agent
    result = run_agent(request.text)

    # 2️⃣ Save to DB
    new_interaction = Interaction(
        hcp_name=result.get("hcp_name", "Unknown"),
        interaction_type=result.get("interaction_type", "Unknown"),
        notes=result.get("notes", ""),
        sentiment=result.get("sentiment", "Unknown"),
        outcome=result.get("outcome", "Unknown"),
        follow_up=result.get("follow_up", "Unknown"),
        priority=result.get("priority", "Normal"),
    )

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    # 3️⃣ Return response
    return {
        "message": "AI processed & saved to DB 🚀",
        "data": result,
        "db_id": new_interaction.id
    }