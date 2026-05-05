from fastapi import APIRouter, HTTPException
from app.services.geo_service import buscar_direccion
 
router = APIRouter(prefix='/mapa', tags=['Mapa'])
 
@router.get('/buscar-direccion')
async def buscar(q: str):
    try:
        resultados = await buscar_direccion(q)
        return {'resultados': resultados}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
