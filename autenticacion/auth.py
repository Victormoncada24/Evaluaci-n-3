import bcrypt
from base_datos.conexion import conectar
from consumo_api.indicadores import consultar_jsonplaceholder

def registrar_usuario(nombre_usuario, contrasena):
    """Registra un usuario con una contraseña encriptada."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Generar hash de la contraseña
    contrasena_hash = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    
    try:
        cursor.execute("INSERT INTO usuarios (nombre_usuario, contrasena_hash) VALUES (%s, %s)", 
                       (nombre_usuario, contrasena_hash))
        conexion.commit()
        print("Usuario registrado con éxito.")
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
    finally:
        conexion.close()

def iniciar_sesion(nombre_usuario, contrasena):
    """Valida las credenciales del usuario."""
    conexion = conectar()
    cursor = conexion.cursor()
    
    try:
        cursor.execute("SELECT contrasena_hash FROM usuarios WHERE nombre_usuario = %s", 
                       (nombre_usuario,))
        resultado = cursor.fetchone()
        
        if resultado and bcrypt.checkpw(contrasena.encode('utf-8'), resultado[0].encode('utf-8')):
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Credenciales inválidas.")
            return False
    except Exception as e:
        print(f"Error en el inicio de sesión: {e}")
    finally:
        conexion.close()

def guardar_albums(albums):
    """Guarda los albums obtenidos en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        for album in albums:
            cursor.execute('''
                INSERT INTO albums (id, user_id, title)
                VALUES (%s, %s, %s)
            ''', (album['id'], album['userId'], album['title']))
        conexion.commit()
    except Exception as e:
        print(f"Error al guardar albums: {e}")
    finally:
        conexion.close()

def guardar_fotos(fotos):
    """Guarda las fotos obtenidas en la base de datos."""
    conexion = conectar()
    cursor = conexion.cursor()

    try:
        for foto in fotos:
            cursor.execute('''
                INSERT INTO fotos (id, album_id, title, url, thumbnail_url)
                VALUES (%s, %s, %s, %s, %s)
            ''', (foto['id'], foto['albumId'], foto['title'], foto['url'], foto['thumbnailUrl']))
        conexion.commit()        
    except Exception as e:
        print(f"Error al guardar fotos: {e}")
    finally:
        
        conexion.close()