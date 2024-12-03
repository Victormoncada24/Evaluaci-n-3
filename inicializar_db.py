import mysql.connector
from base_dedatos.import config

def inicializar_base_datos():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Crear tablas
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        contraseña_hash VARCHAR(255) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS indicadores (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre_indicador VARCHAR(255) NOT NULL,
        valor FLOAT NOT NULL,
        fecha_consulta DATE NOT NULL,
        fecha_registro DATETIME NOT NULL,
        usuario_id INT NOT NULL,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Base de datos inicializada correctamente.")

if __name__ == "__main__":
    inicializar_base_datos()
