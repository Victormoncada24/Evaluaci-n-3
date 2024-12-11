from autenticacion.auth import registrar_usuario, iniciar_sesion, guardar_albums, guardar_fotos
from consumo_api.indicadores import consultar_jsonplaceholder

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
            while True:
                print("=== Menú Principal ===")
                print("1. Consultar y guardar Albums")
                print("2. Consultar y guardar Fotos")
                print("3. Volver")
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    albums = consultar_jsonplaceholder("albums")
                    if albums:
                        guardar_albums(albums[:5])
                elif opcion == "2":
                    fotos = consultar_jsonplaceholder("photos")
                    if fotos:
                        guardar_fotos(fotos[:5])
                elif opcion == "3":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción no válida.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")
mostrar_menu()