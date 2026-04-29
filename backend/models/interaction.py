from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from backend.db.base import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String, index=True)
    notes = Column(String)
    tag = Column(String)  # ✅ ADD THIS
    created_at = Column(DateTime, default=datetime.utcnow)