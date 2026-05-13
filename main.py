from fastapi import FastAPI
from config.database import engine, Base
<<<<<<< HEAD
from app.models import usuario_db, reciclador_db, solicitud_db
from app.controllers import (
    usuario_controller,
    reciclador_controller,
    solicitud_controller,
    geo_controller
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Reciclaje Pereira API",
    description="Sistema que conecta ciudadanos con recicladores en Pereira",
    version="1.0.0"
)

app.include_router(usuario_controller.router)
app.include_router(reciclador_controller.router)
app.include_router(solicitud_controller.router)
app.include_router(geo_controller.router)

@app.get("/", tags=["Inicio"])
def root():
    return {
        "mensaje": "Bienvenido a la API de Reciclaje Pereira",
        "version": "1.0.0",
        "documentacion": "/docs"
    }
=======
from app.models import usuario_db, reciclador_db
from app.controllers import usuario_controller, reciclador_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Reciclaje Pereira API')

app.include_router(usuario_controller.router)
app.include_router(reciclador_controller.router)

@app.get('/')
def root():
    return {'mensaje': 'Bienvenido a la API de Reciclaje Pereira'}
from fastapi import FastAPI
from config.database import engine, Base
from app.models import usuario_db, reciclador_db
from app.controllers import usuario_controller, reciclador_controller

Base.metadata.create_all(bind=engine)

app = FastAPI(title='Reciclaje Pereira API')

app.include_router(usuario_controller.router)
app.include_router(reciclador_controller.router)

@app.get('/')
def root():
    return {'mensaje': 'Bienvenido a la API de Reciclaje Pereira'}
>>>>>>> origin/feature/lina-crud-usuarios
