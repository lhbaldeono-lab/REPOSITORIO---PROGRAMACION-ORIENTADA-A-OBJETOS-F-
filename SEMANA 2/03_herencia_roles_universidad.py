"""
EJEMPLO 3 – HERENCIA
Escenario: Roles dentro de una universidad.

HERENCIA:
- Clase base: MiembroUniversidad
    • nombre
    • correo
    • identificador
- Clases hijas:
    • Estudiante
    • Docente
    • Administrativo

Cada clase hija reutiliza lo de la clase base y agrega sus propios datos.
"""

class MiembroUniversidad:
    def __init__(self, nombre, correo, identificador):
        self.nombre = nombre
        self.correo = correo
        self.identificador = identificador

    def presentar(self):
        return f"{self.nombre} ({self.identificador}) - {self.correo}"


class Estudiante(MiembroUniversidad):
    def __init__(self, nombre, correo, identificador, carrera, nivel):
        super().__init__(nombre, correo, identificador)
        self.carrera = carrera
        self.nivel = nivel

    def info_estudiante(self):
        base = self.presentar()
        return f"{base} | Estudiante de {self.carrera}, Nivel: {self.nivel}"


class Docente(MiembroUniversidad):
    def __init__(self, nombre, correo, identificador, titulo, area):
        super().__init__(nombre, correo, identificador)
        self.titulo = titulo
        self.area = area

    def info_docente(self):
        base = self.presentar()
        return f"{base} | Docente {self.titulo} en el área de {self.area}"


class Administrativo(MiembroUniversidad):
    def __init__(self, nombre, correo, identificador, cargo):
        super().__init__(nombre, correo, identificador)
        self.cargo = cargo

    def info_admin(self):
        base = self.presentar()
        return f"{base} | Personal administrativo - Cargo: {self.cargo}"


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("=== EJEMPLO 3: HERENCIA (Roles universitarios) ===")

    est = Estudiante("María López", "maria@uea.edu.ec", "EST-001", "Ingeniería en Sistemas", "4to nivel")
    doc = Docente("Carlos Pérez", "carlos@uea.edu.ec", "DOC-010", "Magíster", "Programación")
    adm = Administrativo("Ana Torres", "ana@uea.edu.ec", "ADM-100", "Secretaria de Facultad")

    print(est.info_estudiante())
    print(doc.info_docente())
    print(adm.info_admin())

