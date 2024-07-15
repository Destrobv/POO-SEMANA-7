class Recurso:
    def __init__(self, nombre):
        """ Constructor: Inicializa el recurso con un nombre """
        self.nombre = nombre
        print(f"Recurso {self.nombre} ha sido creado.")

    def __del__(self):
        """ Destructor: Realiza limpieza de recursos """
        print(f"Recurso {self.nombre} ha sido destruido.")

class GestorDeRecursos:
    def __init__(self, nombre):
        """ Constructor: Inicializa el gestor y crea un recurso """
        self.nombre = nombre
        self.recurso = Recurso(nombre)
        print(f"Gestor de recursos para {self.nombre} ha sido creado.")

    def __del__(self):
        """ Destructor: Limpia el recurso """
        print(f"Gestor de recursos para {self.nombre} está siendo destruido.")
        del self.recurso

def main():
    gestor1 = GestorDeRecursos("Recurso1")
    gestor2 = GestorDeRecursos("Recurso2")


if __name__ == "__main__":
    main()
