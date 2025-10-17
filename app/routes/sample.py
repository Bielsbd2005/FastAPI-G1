from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.item import Note, NoteCreate
from app.models.note_model import NoteORM

router = APIRouter(prefix="/api/notes", tags=["notes"])


@router.post("/", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(payload: NoteCreate, db: Session = Depends(get_db)):
    """Create a new note."""
    note = NoteORM(title=payload.title, content=payload.content)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("/", response_model=List[Note])
def list_notes(db: Session = Depends(get_db)):
    """List all notes."""
    return db.query(NoteORM).order_by(NoteORM.created_at.desc()).all()


@router.get("/{note_id}", response_model=Note)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note = db.get(NoteORM, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=Note)
def update_note(note_id: int, payload: NoteCreate, db: Session = Depends(get_db)):
    note = db.get(NoteORM, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = payload.title
    note.content = payload.content
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.get(NoteORM, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
