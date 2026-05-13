import re
 
def validar_email(email: str) -> bool:
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, email))
 
def validar_telefono(telefono: str) -> bool:
    return telefono.isdigit() and len(telefono) == 10
 
def validar_estado(estado: str) -> bool:
    estados_validos = ['pendiente', 'en_proceso', 'completada']
    return estado in estados_validos
