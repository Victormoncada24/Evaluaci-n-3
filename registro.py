from autenticacion.hash_util import generar_hash # type: ignore
import mysql.connector
from base_datos.config import config # type: ignore

def registrar_usuario(nombre, contraseña):
    contraseña_hash = generar_hash(contraseña)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute('INSERT INTO usuarios (nombre, contraseña_hash) VALUES (%s, %s)', 
                   (nombre, contraseña_hash))
    conn.commit()
    conn.close()
    print(f"Usuario {nombre} registrado con éxito.")
