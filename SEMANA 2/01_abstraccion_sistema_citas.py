"""
EJEMPLO 1 – ABSTRACCIÓN
Escenario: Sistema de citas médicas en la universidad.

La ABSTRACCIÓN se usa para crear una clase Cita que contiene
solo la información ESENCIAL de una cita:
- paciente
- médico
- fecha
- tipo de servicio

No programamos todo un sistema real (base de datos, interfaz, etc.),
solo el MODELO simplificado de una cita.
"""

class Cita:
    def __init__(self, paciente, medico, fecha, tipo_servicio):
        # Atributos esenciales de una cita
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.tipo_servicio = tipo_servicio
        self.estado = "Programada"

    def resumen(self):
        """Devuelve un resumen legible de la cita."""
        return (f"Cita ({self.estado}) - Paciente: {self.paciente}, "
                f"Médico: {self.medico}, Fecha: {self.fecha}, "
                f"Servicio: {self.tipo_servicio}")

    def reprogramar(self, nueva_fecha):
        """Permite cambiar la fecha de la cita."""
        self.fecha = nueva_fecha
        self.estado = "Reprogramada"

    def cancelar(self):
        """Cambia el estado de la cita a cancelada."""
        self.estado = "Cancelada"


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("=== EJEMPLO 1: ABSTRACCIÓN (Citas médicas) ===")

    cita1 = Cita("Luis Baldeón", "Dra. Ramírez", "10-12-2025", "Medicina General")
    print(cita1.resumen())

    # Reprogramamos la cita
    cita1.reprogramar("15-12-2025")
    print("Después de reprogramar:")
    print(cita1.resumen())

    # Cancelamos la cita
    cita1.cancelar()
    print("Después de cancelar:")
    print(cita1.resumen())
