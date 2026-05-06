from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.solicitud_db import SolicitudDB
from app.models.usuario_db import UsuarioDB
from app.models.schemas import SolicitudCrear, SolicitudRespuesta, SolicitudActualizarEstado
from app.utils.puntos import calcular_puntos
from app.services.geo_service import buscar_direccion
from typing import List

router = APIRouter(prefix="/solicitudes", tags=["Solicitudes"])

# CREAR solicitud
@router.post("/", response_model=SolicitudRespuesta)
async def crear_solicitud(solicitud: SolicitudCrear, db: Session = Depends(get_db)):
    try:
        # Verificar que el usuario existe
        usuario = db.query(UsuarioDB).filter(
            UsuarioDB.id == solicitud.usuario_id
        ).first()
        if not usuario:
            raise HTTPException(
                status_code=404,
                detail="Usuario no encontrado"
            )
        # Verificar la dirección con la API de mapas
        await buscar_direccion(solicitud.direccion)

        nueva = SolicitudDB(
            usuario_id=solicitud.usuario_id,
            direccion=solicitud.direccion,
            descripcion=solicitud.descripcion
        )
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# LISTAR todas las solicitudes
@router.get("/", response_model=List[SolicitudRespuesta])
def listar_solicitudes(db: Session = Depends(get_db)):
    return db.query(SolicitudDB).all()

# OBTENER solicitudes de un usuario
@router.get("/usuario/{usuario_id}", response_model=List[SolicitudRespuesta])
def solicitudes_por_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return db.query(SolicitudDB).filter(
        SolicitudDB.usuario_id == usuario_id
    ).all()

# ACTUALIZAR estado de solicitud
@router.put("/{solicitud_id}/estado", response_model=SolicitudRespuesta)
def actualizar_estado(
    solicitud_id: int,
    datos: SolicitudActualizarEstado,
    db: Session = Depends(get_db)
):
    estados_validos = ["pendiente", "en_proceso", "completada"]
    if datos.estado not in estados_validos:
        raise HTTPException(
            status_code=400,
            detail=f"Estado inválido. Debe ser: {estados_validos}"
        )

    solicitud = db.query(SolicitudDB).filter(
        SolicitudDB.id == solicitud_id
    ).first()
    if not solicitud:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    solicitud.estado = datos.estado
    if datos.reciclador_id:
        solicitud.reciclador_id = datos.reciclador_id

    # Si se completó, sumar puntos al usuario
    if datos.estado == "completada":
        usuario = db.query(UsuarioDB).filter(
            UsuarioDB.id == solicitud.usuario_id
        ).first()
        if usuario:
            puntos = calcular_puntos(solicitud.descripcion)
            usuario.puntos += puntos

    db.commit()
    db.refresh(solicitud)
    return solicitud