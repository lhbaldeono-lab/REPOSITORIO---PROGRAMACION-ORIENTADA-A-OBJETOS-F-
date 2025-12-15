# ---------------------------------------------------------
# Cálculo del promedio semanal del clima
# Enfoque: Programación Orientada a Objetos (POO)
# ---------------------------------------------------------

class ClimaSemanal:
    """
    Clase que representa el clima semanal.
    """

    def __init__(self):
        # Atributo privado (encapsulamiento)
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        """
        Solicita al usuario las temperaturas diarias de la semana.
        """
        for dia in range(1, 8):
            temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.__temperaturas.append(temperatura)

    def calcular_promedio(self):
        """
        Calcula el promedio semanal de las temperaturas.
        """
        return sum(self.__temperaturas) / len(self.__temperaturas)

    def mostrar_resultado(self):
        """
        Muestra el resultado final del promedio.
        """
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
print("=== PROMEDIO SEMANAL DEL CLIMA ===")
print("Enfoque: Programación Orientada a Objetos\n")

clima = ClimaSemanal()
clima.ingresar_temperaturas()
clima.mostrar_resultado()


