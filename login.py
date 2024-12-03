from autenticacion.hash_util import generar_hash # type: ignore
import mysql.connector
from base_datos.config import config # type: ignore

def login_usuario(nombre, contraseña):
    contraseña_hash = generar_hash(contraseña)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('SELECT id FROM usuarios WHERE nombre = %s AND contraseña_hash = %s', 
                   (nombre, contraseña_hash))
    usuario = cursor.fetchone()
    conn.close()

    if usuario:
        print(f"Bienvenido, {nombre}!")
        return usuario[0]  # ID del usuario
    else:
        print("Credenciales incorrectas.")
        return None
