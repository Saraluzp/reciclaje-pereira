def calcular_puntos(descripcion: str = None) -> int:
    if not descripcion:
        return 10  # puntos base
 
    descripcion = descripcion.lower()
 
    if 'electronico' in descripcion or 'electronico' in descripcion:
        return 50
    elif 'vidrio' in descripcion:
        return 30
    elif 'metal' in descripcion or 'lata' in descripcion:
        return 25
    elif 'carton' in descripcion or 'carton' in descripcion:
        return 20
    elif 'papel' in descripcion:
        return 15
    elif 'plastico' in descripcion or 'plastico' in descripcion:
        return 15
    else:
        return 10
