from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get_db
from app.models.schemas import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/recicladores", tags=["Recicladores"])

# Crear reciclador
@router.post("/", response_model=UsuarioResponse, status_code=201)
def crear_reciclador(datos: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.crear_usuario(datos)

# Listar recicladores
@router.get("/", response_model=list[UsuarioResponse])
def listar_recicladores(db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.listar_usuarios()

# Ver un reciclador por ID
@router.get("/{reciclador_id}", response_model=UsuarioResponse)
def obtener_reciclador(reciclador_id: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.obtener_usuario(reciclador_id)

# Actualizar reciclador
@router.put("/{reciclador_id}", response_model=UsuarioResponse)
def actualizar_reciclador(reciclador_id: int, datos: UsuarioCreate, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.actualizar_usuario(reciclador_id, datos.model_dump())

# Eliminar reciclador
@router.delete("/{reciclador_id}")
def eliminar_reciclador(reciclador_id: int, db: Session = Depends(get_db)):
    service = UsuarioService(db)
    return service.eliminar_usuario(reciclador_id)