from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.usuario_db import UsuarioDB
from app.models.schemas import UsuarioCrear, UsuarioRespuesta, UsuarioActualizar
from typing import List
<<<<<<< HEAD

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# CREAR usuario
@router.post("/", response_model=UsuarioRespuesta)
def crear_usuario(usuario: UsuarioCrear, db: Session = Depends(get_db)):
    try:
        # Verificar si el email ya existe
        existe = db.query(UsuarioDB).filter(
            UsuarioDB.email == usuario.email
        ).first()
        if existe:
            raise HTTPException(
                status_code=400,
                detail="Ya existe un usuario con ese email"
            )
        nuevo = UsuarioDB(
            nombre=usuario.nombre,
            email=usuario.email,
            telefono=usuario.telefono,
            direccion=usuario.direccion
        )
=======
 
router = APIRouter(prefix='/usuarios', tags=['Usuarios'])
 
# CREAR usuario
@router.post('/', response_model=UsuarioRespuesta)
def crear_usuario(usuario: UsuarioCrear, db: Session = Depends(get_db)):
    try:
        existe = db.query(UsuarioDB).filter(
            UsuarioDB.email == usuario.email).first()
        if existe:
            raise HTTPException(status_code=400,
                detail='Ya existe un usuario con ese email')
        nuevo = UsuarioDB(
            nombre=usuario.nombre, email=usuario.email,
            telefono=usuario.telefono, direccion=usuario.direccion)
>>>>>>> origin/feature/lina-crud-usuarios
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return nuevo
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
<<<<<<< HEAD

# LISTAR todos los usuarios
@router.get("/", response_model=List[UsuarioRespuesta])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()

# OBTENER un usuario por id
@router.get("/{usuario_id}", response_model=UsuarioRespuesta)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id
    ).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    return usuario

# ACTUALIZAR usuario
@router.put("/{usuario_id}", response_model=UsuarioRespuesta)
def actualizar_usuario(
    usuario_id: int,
    datos: UsuarioActualizar,
    db: Session = Depends(get_db)
):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id
    ).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
=======
 
# LISTAR todos los usuarios
@router.get('/', response_model=List[UsuarioRespuesta])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()
 
# OBTENER usuario por id
@router.get('/{usuario_id}', response_model=UsuarioRespuesta)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    return usuario
 
# ACTUALIZAR usuario
@router.put('/{usuario_id}', response_model=UsuarioRespuesta)
def actualizar_usuario(usuario_id: int, datos: UsuarioActualizar,
                       db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
>>>>>>> origin/feature/lina-crud-usuarios
    if datos.nombre: usuario.nombre = datos.nombre
    if datos.email: usuario.email = datos.email
    if datos.telefono: usuario.telefono = datos.telefono
    if datos.direccion: usuario.direccion = datos.direccion
    db.commit()
    db.refresh(usuario)
    return usuario
<<<<<<< HEAD

# ELIMINAR usuario
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id
    ).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    db.delete(usuario)
    db.commit()
    return {"mensaje": f"Usuario {usuario.nombre} eliminado correctamente"}
=======
 
# ELIMINAR usuario
@router.delete('/{usuario_id}')
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    db.delete(usuario)
    db.commit()
    return {'mensaje': f'Usuario {usuario.nombre} eliminado correctamente'}
>>>>>>> origin/feature/lina-crud-usuarios
