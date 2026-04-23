from .persona import Persona

class Usuario(Persona):
    def __init__(self, nombre, email, telefono, direccion):
        super().__init__(nombre, email, telefono)
        self.direccion = direccion
        self.puntos = 0

    def acumular_puntos(self, cantidad):
        self.puntos += cantidad

    def get_info(self):  # Polimorfismo
        info = super().get_info()
        info["puntos"] = self.puntos
        return info
    