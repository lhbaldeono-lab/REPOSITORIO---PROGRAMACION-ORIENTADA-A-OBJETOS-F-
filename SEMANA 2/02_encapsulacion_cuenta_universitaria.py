"""
EJEMPLO 2 – ENCAPSULACIÓN
Escenario: Cuenta universitaria de un estudiante.

La ENCAPSULACIÓN se usa para PROTEGER la información interna:
- _nombre
- _matricula
- _saldo

Solo se puede acceder o modificar estos datos a través de MÉTODOS
controlados (getters y setters), que validan la información.
"""

class CuentaUniversitaria:
    def __init__(self, nombre, matricula):
        # Atributos "protegidos" (convención con guion bajo)
        self._nombre = nombre
        self._matricula = matricula
        self._saldo = 0.0  # saldo en dólares

    # ========= MÉTODOS GET =========
    def get_nombre(self):
        return self._nombre

    def get_matricula(self):
        return self._matricula

    def get_saldo(self):
        return self._saldo

    # ========= MÉTODOS SET / ACCIONES =========
    def recargar(self, monto):
        """Añade dinero al saldo, validando que el monto sea positivo."""
        if monto > 0:
            self._saldo += monto
            print(f"Se recargaron ${monto:.2f}. Nuevo saldo: ${self._saldo:.2f}")
        else:
            print("El monto de recarga debe ser positivo.")

    def pagar_servicio(self, valor, descripcion):
        """Descuenta un servicio si hay saldo suficiente."""
        if valor <= 0:
            print("El valor del servicio debe ser positivo.")
            return

        if valor > self._saldo:
            print(f"No hay saldo suficiente para pagar {descripcion}. Saldo actual: ${self._saldo:.2f}")
        else:
            self._saldo -= valor
            print(f"Pago realizado: {descripcion} por ${valor:.2f}. Saldo restante: ${self._saldo:.2f}")

    def mostrar_info(self):
        """Muestra información general de la cuenta."""
        print(f"Cuenta de: {self._nombre} (Matrícula: {self._matricula}) - Saldo: ${self._saldo:.2f}")


# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("=== EJEMPLO 2: ENCAPSULACIÓN (Cuenta universitaria) ===")

    cuenta = CuentaUniversitaria("Luis Baldeón", "2025-IS-001")
    cuenta.mostrar_info()

    cuenta.recargar(100)
    cuenta.pagar_servicio(35, "Matrícula parcial")
    cuenta.pagar_servicio(80, "Laboratorio de cómputo")  # aquí debería faltar saldo

    print("Saldo final:", cuenta.get_saldo())
