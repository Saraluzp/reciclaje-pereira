from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from config.database import Base

class SolicitudDB(Base):
    __tablename__ = "solicitudes"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    reciclador_id = Column(Integer, ForeignKey("recicladores.id"), nullable=True)
    direccion = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    estado = Column(String, default="pendiente")
    fecha_creacion = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<Solicitud {self.id} - {self.estado}>"