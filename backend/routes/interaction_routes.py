from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

# In-memory storage
interactions = []

# Request model
class Interaction(BaseModel):
    doctor_name: str
    notes: str

# AI Tag Logic
def generate_tag(notes: str):
    notes = notes.lower()

    if "price" in notes or "pricing" in notes:
        return "💰 Pricing Discussion"
    elif "demo" in notes:
        return "📺 Demo Scheduled"
    elif "follow" in notes:
        return "📞 Follow-up"
    elif "interested" in notes:
        return "🔥 Interested Lead"
    else:
        return "📝 General"

# GET all interactions
@router.get("/interactions")
def get_interactions():
    return interactions

# POST new interaction
@router.post("/interactions")
def add_interaction(data: Interaction):
    new_data = {
        "doctor_name": data.doctor_name,
        "notes": data.notes,
        "tag": generate_tag(data.notes),
        "timestamp": datetime.now().isoformat()
    }

    interactions.append(new_data)

    return new_data