from autenticacion.auth import registrar_usuario, iniciar_sesion, guardar_albums, guardar_fotos
from consumo_api.indicadores import consultar_jsonplaceholder
from modelos.modelos import Album, Photo
from consumo_api.polimorfo_api import post_objeto, put_objeto, delete_objeto, get_objetos
from base_datos.db import crear_album, leer_albums, actualizar_album, eliminar_album, crear_foto, leer_fotos, actualizar_foto, eliminar_foto

def mostrar_menu():
    """Muestra el menú principal del sistema."""
    while True:
        print("=== Menú Principal ===")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Consultar Album o Photos")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese un nombre de usuario: ")
            contrasena = input("Ingrese una contraseña: ")
            registrar_usuario(nombre, contrasena)
        elif opcion == "2":
            nombre = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            iniciar_sesion(nombre, contrasena)
        elif opcion == "3":
            """Muestra el submenú del sistema."""
            while True:
                print("=== Submenú ===")
                print("1. Consultar y guardar Albums")
                print("2. Consultar y guardar Fotos")
                print("3. Mas opciones")
                print("4. Volver")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    albums = consultar_jsonplaceholder("albums")
                    if albums:
                        guardar_albums(albums[:5])
                        albums = consultar_jsonplaceholder("albums")
                        print("Albums guardados correctamente.")
                        print("Primeros 5 albums:")
                        for album in albums[:5]:
                            print(album)                       
                elif opcion == "2":
                    fotos = consultar_jsonplaceholder("photos")
                    if fotos:
                        guardar_fotos(fotos[:5])
                        fotos = consultar_jsonplaceholder("photos")
                        print("Fotos guardadas correctamente.")
                        print("\nPrimeras 5 fotos:")
                        for foto in fotos[:5]:
                            print(foto)
                elif opcion == "3":
                    while True:
                        print("=== Menú Principal ===")
                        print("1. Crear un nuevo álbum")
                        print("2. Leer todos los álbumes")
                        print("3. Actualizar un álbum")
                        print("4. Eliminar un álbum")
                        print("5. Crear una nueva foto")
                        print("6. Leer todas las fotos")
                        print("7. Actualizar una foto")
                        print("8. Eliminar una foto")
                        print("9. Volver")
                        opcion = input("Seleccione una opción: ")

                        if opcion == "1":
                            title = input("Ingrese el título del álbum: ")
                            user_id = int(input("Ingrese el ID del usuario: "))
                            nuevo_album = Album(title=title, user_id=user_id)
                            crear_album(nuevo_album)
                            print("Álbum creado exitosamente.")
                        elif opcion == "2":
                            albums = leer_albums()
                            for album in albums:
                                print(album)
                        elif opcion == "3":
                            album_id = int(input("Ingrese el ID del álbum a actualizar: "))
                            nuevo_titulo = input("Ingrese el nuevo título del álbum: ")
                            nuevo_user_id = int(input("Ingrese el nuevo ID del usuario: "))
                            actualizar_album(album_id, nuevo_titulo, nuevo_user_id)
                            print("Álbum actualizado exitosamente.")
                        elif opcion == "4":
                            album_id = int(input("Ingrese el ID del álbum a eliminar: "))
                            eliminar_album(album_id)
                            print("Álbum eliminado exitosamente.")
                        elif opcion == "5":
                            title = input("Ingrese el título de la foto: ")
                            url = input("Ingrese la URL de la foto: ")
                            thumbnail_url = input("Ingrese la URL de la miniatura: ")
                            albumId = int(input("Ingrese el ID del álbum: "))
                            nueva_foto = Photo(title=title, url=url, thumbnail_url=thumbnail_url, album_id=album_id)
                            crear_foto(nueva_foto)
                            print("Foto creada exitosamente.")
                        elif opcion == "6":
                            fotos = leer_fotos()
                            for foto in fotos:
                                print(foto)
                        elif opcion == "7":
                            foto_id = int(input("Ingrese el ID de la foto a actualizar: "))
                            nuevo_titulo = input("Ingrese el nuevo título de la foto: ")
                            nueva_url = input("Ingrese la nueva URL de la foto: ")
                            nuevo_thumbnail_url = input("Ingrese la nueva URL de la miniatura: ")
                            nuevo_album_id = int(input("Ingrese el nuevo ID del álbum: "))
                            actualizar_foto(foto_id, nuevo_titulo, nueva_url, nuevo_thumbnail_url, nuevo_album_id)
                            print("Foto actualizada exitosamente.")
                        elif opcion == "8":
                            foto_id = int(input("Ingrese el ID de la foto a eliminar: "))
                            eliminar_foto(foto_id)
                            print("Foto eliminada exitosamente.")
                        elif opcion == "9":
                            print("¡Volviendo al menú anterior!")
                            break
                        else:
                            print("Opción no válida. Intente de nuevo.")

                elif opcion == "4":
                    print("¡Regresando al menú principal!")
                    break
                else:
                    print("Opción no válida.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
mostrar_menu()




