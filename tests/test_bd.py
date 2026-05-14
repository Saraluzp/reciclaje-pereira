from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
from app.models.usuario_db import UsuarioDB
from app.models.reciclador_db import RecicladorDB

# Base de datos temporal solo para pruebas
engine_test = create_engine("sqlite:///./test.db")
Base.metadata.create_all(bind=engine_test)
SessionTest = sessionmaker(bind=engine_test)

def test_crear_usuario_en_bd():
    db = SessionTest()
    usuario = UsuarioDB(
        nombre="Lina",
        email="lina@mail.com",
        telefono="3001234567",
        direccion="Calle 20"
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    assert usuario.id is not None
    db.close()

def test_crear_reciclador_en_bd():
    db = SessionTest()
    reciclador = RecicladorDB(
        nombre="Carlos",
        email="carlos@mail.com",
        telefono="3109876543",
        zona="Centro"
    )
    db.add(reciclador)
    db.commit()
    db.refresh(reciclador)
    assert reciclador.disponible == True
    db.close()

def test_usuario_puntos_default():
    db = SessionTest()
    usuario = UsuarioDB(
        nombre="Ana",
        email="ana@mail.com",
        telefono="300",
        direccion="Av. 30"
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    assert usuario.puntos == 0
    db.close()