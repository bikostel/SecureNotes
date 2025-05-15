from fastapi import APIRouter
from pydantic import BaseModel
from cryptography.fernet import Fernet
import os

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY", Fernet.generate_key().decode()).encode()
fernet = Fernet(SECRET_KEY)

fake_notes_db = {}


class NoteCreate(BaseModel):
    title: str
    content: str


class Note(BaseModel):
    id: int
    title: str
    content: str


@router.post("/", response_model=Note)
def create_note(note: NoteCreate):
    note_id = len(fake_notes_db) + 1
    encrypted = fernet.encrypt(note.content.encode()).decode()
    fake_notes_db[note_id] = {
        "title": note.title,
        "content": encrypted
    }
    return {
        "id": note_id,
        "title": note.title,
        "content": note.content
    }


@router.get("/", response_model=list[Note])
def get_notes():
    return [
        {
            "id": note_id,
            "title": note["title"],
            "content": fernet.decrypt(note["content"].encode()).decode()
        }
        for note_id, note in fake_notes_db.items()
    ]
