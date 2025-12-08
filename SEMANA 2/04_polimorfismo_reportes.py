"""
EJEMPLO 4 – POLIMORFISMO
Escenario: Generación de reportes en la universidad.

POLIMORFISMO:
- Todas las clases tienen un método generar()
- Cada clase genera un tipo diferente de reporte:
    • ReporteNotas
    • ReporteAsistencia
    • ReporteFinanciero

Desde una misma función se llama generar() sin importar el tipo
concreto de reporte. Cada objeto responde "a su manera".
"""

class Reporte:
    def generar(self):
        """Método genérico, acá podría estar una implementación básica."""
        print("Generando reporte genérico...")


class ReporteNotas(Reporte):
    def generar(self):
        print("Generando reporte de notas de los estudiantes...")
        print("- Estudiante: Luis | Promedio: 8.9")
        print("- Estudiante: María | Promedio: 9.5")


class ReporteAsistencia(Reporte):
    def generar(self):
        print("Generando reporte de asistencia a clases...")
        print("- Luis: 95% de asistencia")
        print("- María: 100% de asistencia")


class ReporteFinanciero(Reporte):
    def generar(self):
        print("Generando reporte financiero de la facultad...")
        print("- Ingresos por matrículas: $50,000")
        print("- Gastos de laboratorio: $10,000")
        print("- Saldo disponible: $40,000")


def imprimir_reporte(reporte):
    """
    Función que recibe CUALQUIER objeto que tenga el método generar().
    Aquí se ve el polimorfismo: no importa el tipo exacto de reporte.
    """
    print("=== Ejecutando generación de reporte ===")
    reporte.generar()
    print("")  # línea en blanco


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("=== EJEMPLO 4: POLIMORFISMO (Reportes) ===")

    r_notas = ReporteNotas()
    r_asistencia = ReporteAsistencia()
    r_financiero = ReporteFinanciero()

    # Llamamos a la MISMA función con objetos diferentes
    imprimir_reporte(r_notas)
    imprimir_reporte(r_asistencia)
    imprimir_reporte(r_financiero)
