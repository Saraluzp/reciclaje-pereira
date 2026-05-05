# package
# Validaciones de entrada de datos - Lina

def validar_telefono(telefono: str) -> bool:
    """Verifica que el teléfono tenga exactamente 10 dígitos."""
    return telefono.isdigit() and len(telefono) == 10

def validar_email(email: str) -> bool:
    """Verifica que el email tenga formato básico correcto."""
    return "@" in email and "." in email

def validar_barrio_pereira(barrio: str) -> bool:
    """Verifica que el barrio sea de Pereira."""
    barrios = [
        "cuba", "pinares", "centro", "galicia", "alcázares",
        "villasantana", "boston", "el jardín", "olímpica",
        "nacederos", "málaga", "tokio"
    ]
    return barrio.lower() in barrios

def validar_cantidad_kg(cantidad: float) -> bool:
    """Verifica que la cantidad de kg sea positiva."""
    return cantidad > 0