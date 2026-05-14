from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Esquemas de Usuario
class UsuarioCrear(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: str

class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str
    direccion: str
    puntos: int
    class Config:
        from_attributes = True

class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None

# Esquemas de Reciclador
class RecicladorCrear(BaseModel):
    nombre: str
    email: str
    telefono: str
    zona: str

class RecicladorRespuesta(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str
    zona: str
    disponible: bool
    class Config:
        from_attributes = True

class RecicladorActualizar(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    zona: Optional[str] = None
    disponible: Optional[bool] = None

# Esquemas de Solicitud
class SolicitudCrear(BaseModel):
    usuario_id: int
    direccion: str
    descripcion: Optional[str] = None

class SolicitudRespuesta(BaseModel):
    id: int
    usuario_id: int
    reciclador_id: Optional[int] = None
    direccion: str
    descripcion: Optional[str] = None
    estado: str
    fecha_creacion: datetime
    class Config:
        from_attributes = True

class SolicitudActualizarEstado(BaseModel):
    estado: str