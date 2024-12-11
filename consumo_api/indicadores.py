import requests

def consultar_jsonplaceholder(endpoint):
    """Consulta datos del API JSONPlaceholder."""
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        data = respuesta.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar el API: {e}")
        return None

# Consulta de albums
albums = consultar_jsonplaceholder("albums")
print("Primeros 5 albums:")
for album in albums[:5]:
    print(album)

# Consulta de fotos
fotos = consultar_jsonplaceholder("photos")
print("\nPrimeras 5 fotos:")
for foto in fotos[:5]:
    print(foto)