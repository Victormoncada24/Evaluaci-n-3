import mysql.connector

def conectar():
    """Establece la conexión con la base de datos MySQL."""
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",  # Cambia por tu usuario MySQL
        password="",  # Cambia por tu contraseña MySQL
        database="Modulos"
    )
    return conexion

# #def verificar_conexion():
# #    """Verifica si la conexión a la base de datos es exitosa."""
#     try:
#         conexion = conectar()
#         print("Conexión exitosa a la base de datos.")
#         conexion.close()
#     except mysql.connector.Error as err:
#         print(f"Error de conexión: {err}")

# if _name_ == "_main_":
#     verificar_conexion()