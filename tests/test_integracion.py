from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database import Base
from app.models.usuario_db import UsuarioDB
from app.models.reciclador_db import RecicladorDB
from app.models.solicitud_db import SolicitudDB
from app.utils.puntos import calcular_puntos

# Base de datos temporal para pruebas
engine_test = create_engine("sqlite:///./test_integracion.db")
Base.metadata.create_all(bind=engine_test)
SessionTest = sessionmaker(bind=engine_test)

def test_flujo_completo():
    """Prueba el flujo completo: usuario crea solicitud y gana puntos"""
    db = SessionTest()

    # 1. Crear usuario
    usuario = UsuarioDB(
        nombre="Sara",
        email="sara@reciclaje.com",
        telefono="3001234567",
        direccion="Calle 20 Pereira"
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    # 2. Crear reciclador
    reciclador = RecicladorDB(
        nombre="Carlos",
        email="carlos@reciclaje.com",
        telefono="3109876543",
        zona="Centro"
    )
    db.add(reciclador)
    db.commit()
    db.refresh(reciclador)

    # 3. Crear solicitud
    solicitud = SolicitudDB(
        usuario_id=usuario.id,
        reciclador_id=reciclador.id,
        direccion="Calle 20 Pereira",
        descripcion="plastico",
        estado="pendiente"
    )
    db.add(solicitud)
    db.commit()
    db.refresh(solicitud)

    # 4. Completar solicitud y sumar puntos
    solicitud.estado = "completada"
    puntos = calcular_puntos(solicitud.descripcion)
    usuario.puntos += puntos
    db.commit()

    assert solicitud.estado == "completada"
    assert usuario.puntos == 15  # plastico = 15 puntos
    db.close()

def test_calcular_puntos_materiales():
    """Prueba que cada material da los puntos correctos"""
    assert calcular_puntos("electronico") == 50
    assert calcular_puntos("vidrio") == 30
    assert calcular_puntos("metal") == 25
    assert calcular_puntos("carton") == 20
    assert calcular_puntos("papel") == 15
    assert calcular_puntos("plastico") == 15
    assert calcular_puntos("basura") == 10
    assert calcular_puntos(None) == 10

def test_reciclador_disponibilidad():
    """Prueba que el reciclador inicia disponible"""
    db = SessionTest()
    reciclador = RecicladorDB(
        nombre="Ana",
        email="ana@reciclaje.com",
        telefono="300",
        zona="Cuba"
    )
    db.add(reciclador)
    db.commit()
    db.refresh(reciclador)
    assert reciclador.disponible == True
    db.close()