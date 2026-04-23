class Persona:
    def __init__(self, nombre: str, email: str, telefono: str):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    def ___str__(self):
        return f"{self._nombre} ({self._email})"

    def get_info(self):
        return {"nombre": self._nombre, "email": self._email}