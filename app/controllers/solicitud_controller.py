# VER puntos de un usuario
@router.get('/usuario/{usuario_id}/puntos')
def puntos_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(
        UsuarioDB.id == usuario_id
    ).first()
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail='Usuario no encontrado'
        )
    return {
        'usuario_id': usuario_id,
        'nombre': usuario.nombre,
        'puntos': usuario.puntos,
        'nivel': obtener_nivel(usuario.puntos)
    }
 # VER solicitudes por estado
@router.get('/estado/{estado}', response_model=List[SolicitudRespuesta])
def solicitudes_por_estado(estado: str, db: Session = Depends(get_db)):
    estados_validos = ['pendiente', 'en_proceso', 'completada']
    if estado not in estados_validos:
        raise HTTPException(
            status_code=400,
            detail=f'Estado invalido. Debe ser: {estados_validos}'
        )
    return db.query(SolicitudDB).filter(
        SolicitudDB.estado == estado
    ).all()
 

def obtener_nivel(puntos: int) -> str:
    if puntos >= 200:
        return 'Reciclador Experto'
    elif puntos >= 100:
        return 'Reciclador Avanzado'
    elif puntos >= 50:
        return 'Reciclador Intermedio'
    else:
        return 'Reciclador Principiante'
