import httpx
<<<<<<< HEAD

BASE_URL = "https://nominatim.openstreetmap.org"

=======
 
BASE_URL = 'https://nominatim.openstreetmap.org'
 
>>>>>>> origin/feature/jacky-api-puntos
async def buscar_direccion(query: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
<<<<<<< HEAD
                f"{BASE_URL}/search",
                params={
                    "q": query + ", Pereira, Colombia",
                    "format": "json",
                    "limit": 5
                },
                headers={"User-Agent": "ReciclajePereira/1.0"}
=======
                f'{BASE_URL}/search',
                params={
                    'q': query + ', Pereira, Colombia',
                    'format': 'json',
                    'limit': 5,
                    'addressdetails': 1
                },
                headers={'User-Agent': 'ReciclajePereira/1.0'},
                timeout=10.0
>>>>>>> origin/feature/jacky-api-puntos
            )
            response.raise_for_status()
            resultados = response.json()
            if not resultados:
<<<<<<< HEAD
                return {"mensaje": "No se encontró la dirección"}
            return resultados
    except httpx.HTTPError as e:
        raise Exception(f"Error al consultar la API: {e}")
=======
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
>>>>>>> origin/feature/jacky-api-puntos
