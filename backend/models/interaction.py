from sqlalchemy import Column, Integer, String, Text
from db.database import Base


class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_name = Column(String, nullable=False)
    interaction_type = Column(String)
    notes = Column(Text)
    sentiment = Column(String)
    outcome = Column(String)
    follow_up = Column(String)
    priority = Column(String)