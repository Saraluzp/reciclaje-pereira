from fastapi import APIRouter
router = APIRouter(prefix='/recicladores', tags=['Recicladores'])

@router.get('/')
def listar_recicladores():
    return {'mensaje': 'lista de recicladores'}
