# Sistema de Reservas - Ejemplo de Programación Orientada a Objetos
# Autor: Luis Henry Baldeón Ochoa
# Descripción: Programa que modela un sistema básico de reservas usando POO.

class Cliente:
    """
    Clase que representa a un cliente del sistema de reservas.
    """
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def mostrar_datos(self):
        return f"Cliente: {self.nombre} - Cédula: {self.cedula}"


class Reserva:
    """
    Clase que representa una reserva realizada por un cliente.
    """
    def __init__(self, cliente, fecha, lugar):
        self.cliente = cliente
        self.fecha = fecha
        self.lugar = lugar

    def confirmar_reserva(self):
        return (
            "Reserva confirmada\n"
            f"{self.cliente.mostrar_datos()}\n"
            f"Fecha: {self.fecha}\n"
            f"Lugar: {self.lugar}"
        )


# Creación de objetos
cliente1 = Cliente("Luis Henry Baldeón Ochoa", "0605386986")
reserva1 = Reserva(cliente1, "20/12/2025", "Hotel Amazónico")

# Ejecución
print(reserva1.confirmar_reserva())
