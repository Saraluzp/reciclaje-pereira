from app.models.usuario import Usuario
from app.models.reciclador import Reciclador

def test_usuario_acumula_puntos():
    u = Usuario("Lina", "lina@mail.com", "3001234567", "Calle 20")
    u.acumular_puntos(50)
    assert u.puntos == 50

def test_reciclador_cambia_disponibilidad():
    r = Reciclador("Carlos", "carlos@mail.com", "3109876543", "Centro")
    r.cambiar_disponibilidad()
    assert r.disponible == False

def test_herencia_get_info():
    u = Usuario("Ana", "ana@mail.com", "300", "Av. 30")
    info = u.get_info()
    assert "puntos" in info