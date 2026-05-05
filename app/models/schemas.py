from datetime import datetime
 
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
    reciclador_id: Optional[int] = None
