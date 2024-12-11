def manejar_excepcion(func):
    """Decorator para manejar excepciones en las funciones."""
    def envoltura(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Se produjo un error: {e}")
    return envoltura