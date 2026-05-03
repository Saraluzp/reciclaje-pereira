from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

class RecicladorDB(Base):
    __tablename__ = "recicladores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    telefono = Column(String, nullable=False)
    zona = Column(String, nullable=False)
    disponible = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Reciclador {self.nombre} - {self.zona}>"