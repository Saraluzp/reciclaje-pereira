class Persona:
    def __init__(self, nombre: str, email: str, telefono: str):
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    def ___str__(self):
        return f"{self._nombre} ({self._email})"

    def get_info(self):
        return {"nombre": self._nombre, "email": self._email}
    
    # aqi estoy utilizando un constructor  que es mi constructor padre y que le dara la herencia a mis otras dos clases que se llamaran usuario.py y reciclador.py