from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.reciclador_db import RecicladorDB
from app.models.schemas import RecicladorCrear, RecicladorRespuesta, RecicladorActualizar
from typing import List

router = APIRouter(prefix="/recicladores", tags=["Recicladores"])

# CREAR reciclador
@router.post("/", response_model=RecicladorRespuesta)
def crear_reciclador(reciclador: RecicladorCrear, db: Session = Depends(get_db)):
    try:
        existe = db.query(RecicladorDB).filter(
            RecicladorDB.email == reciclador.email
        ).first()
        if existe:
            raise HTTPException(
                status_code=400,
                detail="Ya existe un reciclador con ese email"
            )
        nuevo = RecicladorDB(
            nombre=reciclador.nombre,
            email=reciclador.email,
            telefono=reciclador.telefono,
            zona=reciclador.zona
        )
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# LISTAR todos los recicladores
@router.get("/", response_model=List[RecicladorRespuesta])
def listar_recicladores(db: Session = Depends(get_db)):
    return db.query(RecicladorDB).all()

# OBTENER un reciclador por id
@router.get("/{reciclador_id}", response_model=RecicladorRespuesta)
def obtener_reciclador(reciclador_id: int, db: Session = Depends(get_db)):
    reciclador = db.query(RecicladorDB).filter(
        RecicladorDB.id == reciclador_id
    ).first()
    if not reciclador:
        raise HTTPException(
            status_code=404,
            detail="Reciclador no encontrado"
        )
    return reciclador

# ACTUALIZAR reciclador
@router.put("/{reciclador_id}", response_model=RecicladorRespuesta)
def actualizar_reciclador(
    reciclador_id: int,
    datos: RecicladorActualizar,
    db: Session = Depends(get_db)
):
    reciclador = db.query(RecicladorDB).filter(
        RecicladorDB.id == reciclador_id
    ).first()
    if not reciclador:
        raise HTTPException(
            status_code=404,
            detail="Reciclador no encontrado"
        )
    if datos.nombre: reciclador.nombre = datos.nombre
    if datos.email: reciclador.email = datos.email
    if datos.telefono: reciclador.telefono = datos.telefono
    if datos.zona: reciclador.zona = datos.zona
    if datos.disponible is not None: reciclador.disponible = datos.disponible
    db.commit()
    db.refresh(reciclador)
    return reciclador

# ELIMINAR reciclador
@router.delete("/{reciclador_id}")
def eliminar_reciclador(reciclador_id: int, db: Session = Depends(get_db)):
    reciclador = db.query(RecicladorDB).filter(
        RecicladorDB.id == reciclador_id
    ).first()
    if not reciclador:
        raise HTTPException(
            status_code=404,
            detail="Reciclador no encontrado"
        )
    db.delete(reciclador)
    db.commit()
    return {"mensaje": f"Reciclador {reciclador.nombre} eliminado correctamente"}