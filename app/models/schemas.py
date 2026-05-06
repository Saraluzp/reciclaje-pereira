from pydantic import BaseModel
from typing import Optional
 
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
