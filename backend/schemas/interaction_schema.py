from pydantic import BaseModel

class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    notes: str
    sentiment: str
    outcome: str
    follow_up: str