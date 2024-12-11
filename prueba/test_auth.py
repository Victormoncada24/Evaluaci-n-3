from autenticacion.auth import registrar_usuario, iniciar_sesion

def test_registro():
    registrar_usuario("usuario_prueba", "12345")
    print("Test de registro exitoso.")

def test_login():
    assert iniciar_sesion("usuario_prueba", "12345") == True
    print("Test de inicio de sesión exitoso.")

if _name_ == "_main_":
    test_registro()
    test_login()