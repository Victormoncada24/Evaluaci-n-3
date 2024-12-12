# Proyecto Evaluación 3

## Descripción General
Este proyecto está diseñado para gestionar autenticación, conexión a bases de datos y consumo de APIs. Además, incluye manejo de excepciones y pruebas unitarias para garantizar su funcionalidad.

## Requisitos Previos
- **Python**: Versión 3.10 o superior.
- Dependencias adicionales:
  - (Especificar librerías necesarias, por ejemplo: `requests`, `pytest`, etc.)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone <URL-del-repositorio>
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd Evaluaci-n-3
   ```
3. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto
```
Evaluaci-n-3/
├── config.py               # Configuraciones generales
├── menu.py                 # Lógica del menú principal
├── autenticacion/          # Módulo de autenticación
│   ├── auth.py
│   └── __init__.py
├── base_datos/             # Conexión a la base de datos
│   ├── conexion.py
│   └── __init__.py
├── consumo_api/            # Consumo de APIs externas
│   ├── indicadores.py
│   └── __init__.py
├── excepciones/            # Manejo de excepciones personalizadas
│   └── manejador.py
└── prueba/                 # Pruebas unitarias
    └── test_auth.py
```

## Uso
1. Ejecuta el archivo principal:
   ```bash
   python menu.py
   ```
2. Sigue las instrucciones en pantalla para interactuar con el programa.

## Ejecución de Pruebas
Para ejecutar las pruebas unitarias, utiliza:
```bash
pytest prueba/
```

