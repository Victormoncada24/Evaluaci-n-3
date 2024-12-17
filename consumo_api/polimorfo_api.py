import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def post_objeto(objeto, endpoint):
    """Crea un objeto (POST) en el API."""
    url = f"{BASE_URL}/{endpoint}"
    response = requests.post(url, json=objeto.to_dict())
    if response.status_code == 201:
        print(f"{objeto.__class__.__name__} creado exitosamente: {response.json()}")
    return response

def put_objeto(objeto, endpoint):
    """Actualiza un objeto existente (PUT) en el API."""
    if not objeto.id:
        raise ValueError("Se requiere un ID para actualizar el objeto.")
    url = f"{BASE_URL}/{endpoint}/{objeto.id}"
    response = requests.put(url, json=objeto.to_dict())
    if response.status_code == 200:
        print(f"{objeto.__class__.__name__} actualizado exitosamente: {response.json()}")
    return response

def delete_objeto(objeto_id, endpoint):
    """Elimina un objeto (DELETE) en el API."""
    url = f"{BASE_URL}/{endpoint}/{objeto_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Objeto con ID {objeto_id} eliminado exitosamente.")
    return response

def get_objetos(endpoint, clase_modelo):
    """Obtiene una lista de objetos y los convierte en instancias de la clase modelo."""
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        objetos = [clase_modelo(**item) for item in response.json()]
        return objetos
    return []
