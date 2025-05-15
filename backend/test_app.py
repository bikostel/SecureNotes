# backend/test_app.py

from fastapi.testclient import TestClient
import sys
import os

# Asegura que se puede importar desde backend/
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app import app

client = TestClient(app)

def test_create_and_get_note():
    # Crear una nota
    response = client.post("/notes", json={
        "title": "Nota de prueba",
        "content": "Contenido secreto"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Nota de prueba"
    assert data["content"] == "Contenido secreto"
    note_id = data["id"]

    # Obtener las notas
    response = client.get("/notes")
    assert response.status_code == 200
    notes = response.json()
    assert any(
        note["id"] == note_id and note["content"] == "Contenido secreto"
        for note in notes
    )
