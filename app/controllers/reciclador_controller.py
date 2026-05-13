# VER recicladores disponibles
@router.get('/disponibles/', response_model=List[RecicladorRespuesta])
def recicladores_disponibles(db: Session = Depends(get_db)):
    return db.query(RecicladorDB).filter(
        RecicladorDB.disponible == True
    ).all()
 
# VER recicladores por zona
@router.get('/zona/{zona}', response_model=List[RecicladorRespuesta])
def recicladores_por_zona(zona: str, db: Session = Depends(get_db)):
    recicladores = db.query(RecicladorDB).filter(
        RecicladorDB.zona.ilike(f'%{zona}%')
    ).all()
    if not recicladores:
        raise HTTPException(
            status_code=404,
            detail=f'No hay recicladores en la zona: {zona}'
        )
    return recicladores
