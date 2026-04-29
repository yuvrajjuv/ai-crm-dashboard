from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.session import get_db
from backend.models.interaction import Interaction
from backend.agents.langgraph_agent import generate_tag

router = APIRouter(prefix="/interactions", tags=["Interactions"])


@router.post("/")
def create_interaction(doctor_name: str, notes: str, db: Session = Depends(get_db)):
    
    # 🔥 AI TAG GENERATE
    tag = generate_tag(notes)

    interaction = Interaction(
        doctor_name=doctor_name,
        notes=notes,
        tag=tag
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return {
        "doctor_name": doctor_name,
        "notes": notes,
        "tag": tag
    }


@router.get("/")
def get_interactions(db: Session = Depends(get_db)):
    return db.query(Interaction).all()