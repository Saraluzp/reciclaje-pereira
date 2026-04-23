from fastapi import FastAPI
from config.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reciclaje Pereira API")

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de Reciclaje Pereira"}