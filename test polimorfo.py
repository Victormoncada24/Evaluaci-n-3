from modelos.modelos import Album, Photo
from consumo_api.polimorfo_api import post_objeto, put_objeto, delete_objeto, get_objetos

# Crear un nuevo álbum
nuevo_album = Album(title="Nuevo Álbum", userId=1)
post_objeto(nuevo_album, "albums")

# Actualizar un álbum existente
album_actualizado = Album(id=1, title="Título Actualizado", userId=1)
put_objeto(album_actualizado, "albums")

# Eliminar un álbum
delete_objeto(1, "albums")

# Obtener y mostrar albums
albums = get_objetos("albums", Album)
print("Albums obtenidos:", albums)

# Crear una nueva foto
nueva_foto = Photo(title="Nueva Foto", url="https://example.com/photo.jpg", albumId=1)
post_objeto(nueva_foto, "photos")

# Obtener y mostrar fotos
fotos = get_objetos("photos", Photo)
print("Fotos obtenidas:", fotos)