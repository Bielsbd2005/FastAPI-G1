from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class NoteORM(Base):
    """SQLAlchemy model for persisting notes."""

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(String, nullable=False)
    owner = Column(String(100), nullable=False, index=True, default="anonymous")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
