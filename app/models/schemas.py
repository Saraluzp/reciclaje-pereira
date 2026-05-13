<<<<<<< HEAD
<<<<<<< HEAD
from pydantic import BaseModel, EmailStr
from typing import Optional
from typing import Optional
from datetime import datetime

=======
from pydantic import BaseModel
from typing import Optional
 
>>>>>>> origin/feature/lina-crud-usuarios
# Esquemas de Usuario
class UsuarioCrear(BaseModel):
    nombre: str
    email: str
    telefono: str
    direccion: str
<<<<<<< HEAD

=======
 
>>>>>>> origin/feature/lina-crud-usuarios
class UsuarioRespuesta(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str
    direccion: str
    puntos: int
<<<<<<< HEAD

    class Config:
        from_attributes = True

=======
    class Config:
        from_attributes = True
 
>>>>>>> origin/feature/lina-crud-usuarios
class UsuarioActualizar(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
<<<<<<< HEAD

=======
 
>>>>>>> origin/feature/lina-crud-usuarios
# Esquemas de Reciclador
class RecicladorCrear(BaseModel):
    nombre: str
    email: str
    telefono: str
    zona: str
<<<<<<< HEAD

=======
 
>>>>>>> origin/feature/lina-crud-usuarios
class RecicladorRespuesta(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str
    zona: str
    disponible: bool
<<<<<<< HEAD

    class Config:
        from_attributes = True

=======
    class Config:
        from_attributes = True
 
>>>>>>> origin/feature/lina-crud-usuarios
class RecicladorActualizar(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    zona: Optional[str] = None
    disponible: Optional[bool] = None
<<<<<<< HEAD

=======
from pydantic import BaseModel
from typing import Optional


from datetime import datetime
 
>>>>>>> origin/feature/jacky-api-puntos
# Esquemas de Solicitud
class SolicitudCrear(BaseModel):
    usuario_id: int
    direccion: str
    descripcion: Optional[str] = None
<<<<<<< HEAD

=======
 
>>>>>>> origin/feature/jacky-api-puntos
class SolicitudRespuesta(BaseModel):
    id: int
    usuario_id: int
    reciclador_id: Optional[int] = None
    direccion: str
    descripcion: Optional[str] = None
    estado: str
    fecha_creacion: datetime
<<<<<<< HEAD

    class Config:
        from_attributes = True

class SolicitudActualizarEstado(BaseModel):
    estado: str
    reciclador_id: Optional[int] = None
=======
>>>>>>> origin/feature/lina-crud-usuarios
=======
    class Config:
        from_attributes = True
 
class SolicitudActualizarEstado(BaseModel):
    estado: str
    reciclador_id: Optional[int] = None
>>>>>>> origin/feature/jacky-api-puntos
