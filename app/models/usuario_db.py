from sqlalchemy import Column, Integer, String
from config.database import Base

class UsuarioDB(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefono = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    puntos = Column(Integer, default=0)

    def __repr__(self):
        return f"<Usuario {self.nombre} - {self.email}>"