from fastapi import APIRouter

router = APIRouter(prefix="/recicladores", tags=["Recicladores"])

recicladores_db = []

# GET - Listar todos
@router.get("/")
def listar_recicladores():
    return recicladores_db

# POST - Crear reciclador
@router.post("/")
def crear_reciclador(reciclador: dict):
    recicladores_db.append(reciclador)
    return {"mensaje": "Reciclador creado", "reciclador": reciclador}

# GET - Ver uno por ID
@router.get("/{reciclador_id}")
def obtener_reciclador(reciclador_id: int):
    for r in recicladores_db:
        if r.get("id") == reciclador_id:
            return r
    return {"mensaje": "Reciclador no encontrado"}

# PUT - Actualizar
@router.put("/{reciclador_id}")
def actualizar_reciclador(reciclador_id: int, datos: dict):
    for r in recicladores_db:
        if r.get("id") == reciclador_id:
            r.update(datos)
            return {"mensaje": "Reciclador actualizado", "reciclador": r}
    return {"mensaje": "Reciclador no encontrado"}

# DELETE - Eliminar
@router.delete("/{reciclador_id}")
def eliminar_reciclador(reciclador_id: int):
    for r in recicladores_db:
        if r.get("id") == reciclador_id:
            recicladores_db.remove(r)
            return {"mensaje": "Reciclador eliminado"}
    return {"mensaje": "Reciclador no encontrado"}