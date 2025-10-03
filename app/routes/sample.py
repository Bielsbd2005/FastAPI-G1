from fastapi import APIRouter, HTTPException, status
from typing import List
from datetime import datetime
from app.models.item import Note, NoteCreate

router = APIRouter(prefix="/api/notes", tags=["notes"])

# In-memory "database"
_notes: List[Note] = []
_next_id = 1


@router.post("/", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate):
    """Create a new note."""
    global _next_id
    note = Note(id=_next_id, title=payload.title, content=payload.content, created_at=datetime.utcnow())
    _notes.append(note)
    _next_id += 1
    return note


@router.get("/", response_model=List[Note])
def list_notes():
    """List all notes."""
    return _notes


@router.get("/{note_id}", response_model=Note)
def get_note(note_id: int):
    for n in _notes:
        if n.id == note_id:
            return n
    raise HTTPException(status_code=404, detail="Note not found")


@router.put("/{note_id}", response_model=Note)
def update_note(note_id: int, payload: NoteCreate):
    for idx, n in enumerate(_notes):
        if n.id == note_id:
            updated = Note(id=n.id, title=payload.title, content=payload.content, created_at=n.created_at)
            _notes[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Note not found")


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int):
    for idx, n in enumerate(_notes):
        if n.id == note_id:
            _notes.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Note not found")
