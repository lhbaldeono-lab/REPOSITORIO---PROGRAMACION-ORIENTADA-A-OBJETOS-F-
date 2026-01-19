"""
Tarea: Aplicación de Conceptos de POO en Python
Conceptos incluidos:
- Definición de clase y objeto
- Herencia (Empleado -> EmpleadoPorHoras)
- Encapsulación (atributo privado + getters/setters)
- Polimorfismo (método sobrescrito calcular_pago)
"""

class Empleado:
    """
    Clase base (Herencia): Empleado será la clase padre.
    Encapsulación: __salario_base es un atributo privado.
    """

    def __init__(self, nombre: str, cedula: str, salario_base: float):
        self.nombre = nombre
        self.cedula = cedula
        self.__salario_base = salario_base  # Atributo privado (encapsulación)

    # Getter (obtener salario)
    def get_salario_base(self) -> float:
        return self.__salario_base

    # Setter (modificar salario con validación)
    def set_salario_base(self, nuevo_salario: float) -> None:
        if nuevo_salario < 0:
            raise ValueError("El salario base no puede ser negativo.")
        self.__salario_base = nuevo_salario

    # Método que luego será polimórfico (se sobrescribe en clase hija)
    def calcular_pago(self) -> float:
        """
        Para un empleado fijo, el pago es su salario base.
        """
        return self.__salario_base

    def mostrar_info(self) -> str:
        return f"Empleado: {self.nombre} | Cédula: {self.cedula} | Pago: ${self.calcular_pago():.2f}"


class EmpleadoPorHoras(Empleado):
    """
    Clase derivada (Herencia): hereda de Empleado.
    Polimorfismo: sobrescribe calcular_pago().
    """

    def __init__(self, nombre: str, cedula: str, salario_base: float, horas_trabajadas: int, pago_por_hora: float):
        super().__init__(nombre, cedula, salario_base)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_pago(self) -> float:
        """
        Polimorfismo:
        En lugar de devolver el salario base, calcula pago por horas + base.
        """
        return self.get_salario_base() + (self.horas_trabajadas * self.pago_por_hora)

    def mostrar_info(self) -> str:
        return (
            f"Empleado por horas: {self.nombre} | Cédula: {self.cedula} | "
            f"Horas: {self.horas_trabajadas} | Pago total: ${self.calcular_pago():.2f}"
        )


def main():
    print("===== TAREA POO - SEMANA 6 =====\n")

    # Creación de objetos (instancias)
    empleado_fijo = Empleado("Ana Torres", "0102030405", 500.00)
    empleado_horas = EmpleadoPorHoras("Luis Baldeón", "1850499243", 200.00, 40, 5.50)

    # Mostrar información (polimorfismo: ambos usan calcular_pago, pero cada uno responde diferente)
    print(empleado_fijo.mostrar_info())
    print(empleado_horas.mostrar_info())

    print("\n--- Probando encapsulación (setter) ---")
    empleado_fijo.set_salario_base(550.00)
    print("Nuevo salario base del empleado fijo:", empleado_fijo.get_salario_base())
    print(empleado_fijo.mostrar_info())


if __name__ == "__main__":
    main()
