from autenticacion.registro import registrar_usuario # type: ignore
from autenticacion.login import login_usuario # type: ignore
from consultas.api_client import consultar_indicador # type: ignore
from consultas.registros import registrar_indicador # type: ignore

def main():
    print("Sistema de Gestión de Empleados")
    usuario_id = login_usuario("admin", "password123")
    
    if usuario_id:
        api_url = "https://api.indicadores.com"  # URL real de la API
        indicador = "uf"
        datos = consultar_indicador(api_url, indicador)

        if datos:
            registrar_indicador(usuario_id, indicador, datos["valor"], datos["fecha"])
        else:
            print("No se pudo obtener el indicador.")

if __name__ == "__main__":
    main()
