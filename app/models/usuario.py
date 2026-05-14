from .persona import Persona

class Usuario(Persona):
    """
    Clase que representa un ciudadano registrado en el sistema.
    Hereda de Persona y agrega funcionalidades de reciclaje.
    """
    def __init__(self, nombre: str, email: str, telefono: str, direccion: str):
        super().__init__(nombre, email, telefono)
        self.direccion = direccion
        self.puntos = 0

    def acumular_puntos(self, cantidad: int) -> None:
        self.puntos += cantidad

    def get_info(self) -> dict:
        info = super().get_info()
        info["puntos"] = self.puntos
        info["direccion"] = self.direccion
        return info