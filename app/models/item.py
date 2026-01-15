from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class NoteBase(BaseModel):
    title: str
    content: str


class NoteCreate(NoteBase):
    """Request body for creating/updating a note"""
    pass


class Note(NoteBase):
    id: int
    owner: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    # Pydantic v2 uses `model_config` with `from_attributes`.
    # This code targets Pydantic v2 in the test/runtime environment.
    model_config = {"from_attributes": True}
