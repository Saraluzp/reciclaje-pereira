pip install pydantic[email]
pip freeze > requirements.txt

@app.get('/')
def root():
    from fastapi import FastAPI
    from config.database import engine, Base
    from app.models import usuario_db, reciclador_db
    from app.controllers import usuario_controller, reciclador_controller
    Base.metadata.create_all(bind=engine)
    app = FastAPI(title='Reciclaje Pereira API')
    app.include_router(usuario_controller.router)
    app.include_router(reciclador_controller.router)
    return {'mensaje': 'Bienvenido a la API de Reciclaje Pereira'}

