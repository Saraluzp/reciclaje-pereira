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
                    'limit': 5,
                    'addressdetails': 1
                },
                headers={'User-Agent': 'ReciclajePereira/1.0'},
                timeout=10.0
            )
            response.raise_for_status()
            resultados = response.json()
            if not resultados:
                return []
            return [
                {
                    'nombre': r.get('display_name', ''),
                    'latitud': r.get('lat', ''),
                    'longitud': r.get('lon', ''),
                    'tipo': r.get('type', ''),
                }
                for r in resultados
            ]
    except httpx.TimeoutException:
        raise Exception('La API de mapas tardo demasiado en responder')
    except httpx.HTTPError as e:
        raise Exception(f'Error al consultar la API: {e}')