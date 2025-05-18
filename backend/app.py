k# backend/app.py

from fastapi import FastAPI
from backend.routes import auth, notes


app = FastAPI(
    title="SecureNotes API",
    description="API segura para tomar y consultar notas cifradas",
    version="1.0.0"
)

# Incluir routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])


# Healthcheck para Docker
@app.get("/health")
def health():
    return {"status": "ok"}


# Endpoint raíz para pruebas de vida
@app.get("/")
def read_root():
    return {"message": "SecureNotes backend funcionando correctamente."}

