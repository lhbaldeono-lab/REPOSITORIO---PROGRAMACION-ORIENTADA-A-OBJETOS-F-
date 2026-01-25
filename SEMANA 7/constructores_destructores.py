"""
Programa: Implementación de Constructores y Destructores en Python
Descripción:
Este programa demuestra el uso del constructor (__init__) y del destructor (__del__)
dentro de una clase, mostrando el ciclo de vida de un objeto.
"""

class Archivo:
    def __init__(self, nombre_archivo):
        """
        Constructor de la clase Archivo.
        Se ejecuta automáticamente al crear un objeto.
        Inicializa el nombre del archivo.
        """
        self.nombre_archivo = nombre_archivo
        print(f"Archivo '{self.nombre_archivo}' creado correctamente.")

    def trabajar(self):
        """
        Método que simula el uso del archivo.
        """
        print(f"Trabajando con el archivo '{self.nombre_archivo}'.")

    def __del__(self):
        """
        Destructor de la clase Archivo.
        Se ejecuta cuando el objeto deja de existir.
        Simula la liberación de recursos.
        """
        print(f"Archivo '{self.nombre_archivo}' cerrado y recursos liberados.")


# Creación del objeto
archivo = Archivo("datos.txt")

# Uso del objeto
archivo.trabajar()

# Eliminación del objeto para activar el destructor
del archivo
