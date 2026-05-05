from fastapi import FastAPI
from app.controllers import usuarios, recicladores

application = FastAPI(title='Reciclaje Pereira API')

application.include_router(usuarios.router)
application.include_router(recicladores.router)

@application.get('/')
def root():
    return {'mensaje': 'Bienvenido a la API de Reciclaje Pereira'}
