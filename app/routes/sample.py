from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.item import Note, NoteCreate
from app.models.note_model import NoteORM
from app.routes.auth import get_current_username

router = APIRouter(prefix="/api/notes", tags=["notes"])


@router.post("/", response_model=Note, status_code=status.HTTP_201_CREATED)
def create_note(
    payload: NoteCreate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username),
):
    """Create a new note."""
    note = NoteORM(
        title=payload.title, content=payload.content, owner=username
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.get("/", response_model=List[Note])
def list_notes(
    search: Optional[str] = None,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username),
):
    """List all notes, optionally filtering by title."""
    query = db.query(NoteORM).filter(NoteORM.owner == username)
    if search:
        # Case-insensitive search for the search term anywhere in the title
        query = query.filter(NoteORM.title.ilike(f"%{search}%"))
    return query.order_by(NoteORM.created_at.desc()).all()


@router.get("/{note_id}", response_model=Note)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username),
):
    note = db.get(NoteORM, note_id)
    if not note or note.owner != username:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=Note)
def update_note(
    note_id: int,
    payload: NoteCreate,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username),
):
    note = db.get(NoteORM, note_id)
    if not note or note.owner != username:
        raise HTTPException(status_code=404, detail="Note not found")
    note.title = payload.title
    note.content = payload.content
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    username: str = Depends(get_current_username),
):
    note = db.get(NoteORM, note_id)
    if not note or note.owner != username:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
