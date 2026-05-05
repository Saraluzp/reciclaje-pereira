import httpx
 
BASE_URL = 'https://nominatim.openstreetmap.org'
 
async def buscar_direccion(query: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f'{BASE_URL}/search',
                params={
                    'q': query + ', Pereira, Colombia',
                    'format': 'json',
                    'limit': 5
                },
                headers={'User-Agent': 'ReciclajePereira/1.0'}
            )
            response.raise_for_status()
            resultados = response.json()
            if not resultados:
                return {'mensaje': 'No se encontro la direccion'}
            return resultados
    except httpx.HTTPError as e:
        raise Exception(f'Error al consultar la API: {e}')
