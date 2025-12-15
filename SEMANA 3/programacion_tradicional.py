# ---------------------------------------------------------
# Cálculo del promedio semanal del clima
# Enfoque: Programación Tradicional (uso de funciones)
# ---------------------------------------------------------

def ingresar_temperaturas():
    """
    Solicita al usuario las temperaturas diarias de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    temperaturas = []

    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio semanal de una lista de temperaturas.
    """
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


def main():
    """
    Función principal del programa.
    """
    print("=== PROMEDIO SEMANAL DEL CLIMA ===")
    print("Enfoque: Programación Tradicional\n")

    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)

    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f} °C")


# Ejecución del programa
main()

