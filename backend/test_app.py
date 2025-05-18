# backend/test_app.py

import sys
import os
from fastapi.testclient import TestClient

# Asegura que se puede importar desde backend/
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
))

from backend.app import app  # noqa: E402

client = TestClient(app)


def test_create_and_get_note():
    # Crear una nota
    response = client.post("/notes", json={
        "title": "Nota de prueba",
        "content": "Contenido secreto"
    })
assert response.status_code == 200  # nosec
data = response.json()
assert data["title"] == "Nota de prueba"  # nosec
assert data["content"] == "Contenido secreto"  # nosec
note_id = data["id"]

# Obtener las notas
response = client.get("/notes")
assert response.status_code == 200  # nosec
notes = response.json()
assert any(  # nosec
    note["id"] == note_id and note["content"] == "Contenido secreto"
    for note in notes
)
