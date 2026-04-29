from sqlalchemy import Column, Integer, String
from db.database import Base

class HCP(Base):
    __tablename__ = "hcps"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialty = Column(String)
    hospital = Column(String)