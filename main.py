from fastapi import FastAPI
from config.database import engine, Base

from app.models import usuario_db, reciclador_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reciclaje Pereira API")

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Reciclaje Pereira"}