from .persona import Persona

class Reciclador(Persona):
    def __init__(self, nombre, email, telefono, zona):
        super().__init__(nombre, email, telefono)
        self.zona = zona
        self.disponible = True

    def cambiar_disponibilidad(self):
        self.disponible = not self.disponible

    def get_info(self):  # Polimorfismo
        info = super().get_info()
        info["zona"] = self.zona
        info["disponible"] = self.disponible
        return info