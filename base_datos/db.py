import mysql.connector
from modelos.modelos import Album, Photo

# Configuración de la conexión a MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # Cambia esto por tu usuario de MySQL
        password="",    # Cambia esto por tu contraseña de MySQL
        database="Modulos"
    )

# CRUD para Álbumes
def crear_album(album):
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = "INSERT INTO albums (title, user_id) VALUES (%s, %s)"
    cursor.execute(query, (album.title, album.user_id))
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_albums():
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM albums")
    albums = [Album(**row) for row in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return albums

def actualizar_album(album_id, nuevo_titulo, nuevo_user_id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = "UPDATE albums SET title = %s, user_id = %s WHERE id = %s"
    cursor.execute(query, (nuevo_titulo, nuevo_user_id, album_id))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_album(album_id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = "DELETE FROM albums WHERE id = %s"
    cursor.execute(query, (album_id,))
    conexion.commit()
    cursor.close()
    conexion.close()

# CRUD para Fotos
def crear_foto(foto):
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = "INSERT INTO photos (title, url, thumbnail_url, album_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (foto.title, foto.url, foto.thumbnail_url, foto.album_id))
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_fotos():
    conexion = conectar_db()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM photos")
    photos = [Photo(**row) for row in cursor.fetchall()]
    cursor.close()
    conexion.close()
    return photos

def actualizar_foto(foto_id, nuevo_titulo, nueva_url, nuevo_thumbnail_url, nuevo_album_id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = """
        UPDATE photos 
        SET title = %s, url = %s, thumbnail_url = %s, album_id = %s 
        WHERE id = %s
    """
    cursor.execute(query, (nuevo_titulo, nueva_url, nuevo_thumbnail_url, nuevo_album_id, foto_id))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_foto(foto_id):
    conexion = conectar_db()
    cursor = conexion.cursor()
    query = "DELETE FROM photos WHERE id = %s"
    cursor.execute(query, (foto_id,))
    conexion.commit()
    cursor.close()
    conexion.close()
