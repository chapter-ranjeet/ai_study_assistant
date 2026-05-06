from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String)
    content = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"))