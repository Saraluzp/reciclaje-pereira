from fastapi import APIRouter, HTTPException
from app.services.geo_service import buscar_direccion
 
router = APIRouter(prefix='/mapa', tags=['Mapa'])
 
@router.get('/buscar-direccion')
async def buscar(q: str):
    if not q or len(q.strip()) < 3:
        raise HTTPException(
            status_code=400,
            detail='La busqueda debe tener al menos 3 caracteres'
        )
    try:
        resultados = await buscar_direccion(q)
        if not resultados:
            return {
                'mensaje': 'No se encontraron resultados',
                'busqueda': q,
'resultados': []
            }
        return {
            'busqueda': q,
            'total': len(resultados),
            'resultados': resultados
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
@router.get('/pereira/zonas')
def zonas_pereira():
    return {
        'ciudad': 'Pereira',
        'zonas': [
            {'nombre': 'Centro', 'descripcion': 'Centro historico de Pereira'},
            {'nombre': 'Cuba', 'descripcion': 'Comuna Cuba'},
            {'nombre': 'Dosquebradas', 'descripcion': 'Municipio aledano'},
            {'nombre': 'El Poblado', 'descripcion': 'Zona residencial'},
            {'nombre': 'Villasantana', 'descripcion': 'Comuna Villasantana'},
            {'nombre': 'Boston', 'descripcion': 'Barrio Boston'},
            {'nombre': 'Alamos', 'descripcion': 'Sector Alamos'},
        ]
    }
