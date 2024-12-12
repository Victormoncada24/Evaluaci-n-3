from autenticacion.auth import registrar_usuario, iniciar_sesion

def test_registro():
    registrar_usuario("admin", "12345")
    print("Test de registro exitoso.")

def test_login():
    assert iniciar_sesion("admin", "12345") == True
    print("Test de inicio de sesión exitoso.")

test_registro()
test_login()