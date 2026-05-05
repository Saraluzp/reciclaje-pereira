from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

# Lista temporal (después Sara conecta la base de datos)
usuarios_db = []

# GET - Listar todos los usuarios
@router.get("/")
def listar_usuarios():
    return usuarios_db

# POST - Crear usuario
@router.post("/")
def crear_usuario(usuario: dict):
    usuarios_db.append(usuario)
    return {"mensaje": "Usuario creado", "usuario": usuario}

# GET - Ver un usuario por ID
@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    for u in usuarios_db:
        if u.get("id") == usuario_id:
            return u
    return {"mensaje": "Usuario no encontrado"}

# PUT - Actualizar usuario
@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, datos: dict):
    for u in usuarios_db:
        if u.get("id") == usuario_id:
            u.update(datos)
            return {"mensaje": "Usuario actualizado", "usuario": u}
    return {"mensaje": "Usuario no encontrado"}

# DELETE - Eliminar usuario
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    for u in usuarios_db:
        if u.get("id") == usuario_id:
            usuarios_db.remove(u)
            return {"mensaje": "Usuario eliminado"}
    return {"mensaje": "Usuario no encontrado"}