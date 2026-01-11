"""
Programa: Calculadora de área y perímetro de un rectángulo.

Descripción:
Este programa solicita al usuario el ancho y el alto de un rectángulo, valida que los valores sean positivos,
calcula el área y el perímetro, y muestra los resultados. También pregunta si el usuario desea repetir el cálculo.
"""

def es_numero_positivo(valor_texto):
    """
    Verifica si una cadena puede convertirse a un número float positivo.
    Retorna True si es positivo, caso contrario False.
    """
    try:
        valor_numerico = float(valor_texto)
        return valor_numerico > 0
    except ValueError:
        return False


def pedir_float_positivo(mensaje):
    """
    Pide al usuario un número positivo (float). Repite la solicitud hasta que sea válido.
    """
    while True:
        entrada_usuario = input(mensaje)  # string
        if es_numero_positivo(entrada_usuario):  # boolean
            return float(entrada_usuario)  # float
        print("Error: Ingresa un número válido y mayor que 0.")


def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo.
    """
    return ancho * alto


def calcular_perimetro_rectangulo(ancho, alto):
    """
    Calcula el perímetro de un rectángulo.
    """
    return 2 * (ancho + alto)


def main():
    print("=== Calculadora de Rectángulo (Área y Perímetro) ===")

    continuar = True  # boolean

    while continuar:
        # Solicitar datos (float) con validación
        ancho = pedir_float_positivo("Ingresa el ancho del rectángulo: ")
        alto = pedir_float_positivo("Ingresa el alto del rectángulo: ")

        # Cálculos
        area = calcular_area_rectangulo(ancho, alto)          # float
        perimetro = calcular_perimetro_rectangulo(ancho, alto) # float

        # Ejemplo de integer (conteo simple)
        cantidad_decimales = 2  # int

        # Mostrar resultados (string formateado)
        print(f"\nResultados:")
        print(f"- Ancho: {ancho:.{cantidad_decimales}f}")
        print(f"- Alto: {alto:.{cantidad_decimales}f}")
        print(f"- Área: {area:.{cantidad_decimales}f}")
        print(f"- Perímetro: {perimetro:.{cantidad_decimales}f}\n")

        # Preguntar si desea repetir
        respuesta = input("¿Deseas calcular otro rectángulo? (s/n): ").strip().lower()  # string
        continuar = (respuesta == "s")  # boolean

    print("\nPrograma finalizado. ¡Gracias!")


if __name__ == "__main__":
    main()
