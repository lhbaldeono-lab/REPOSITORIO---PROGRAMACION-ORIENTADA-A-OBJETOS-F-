# main.py
# Interfaz de usuario por consola (menú)

from inventario import Inventario


def pedir_int(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Debes ingresar un número entero.")


def pedir_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Debes ingresar un número (ej: 2.50).")


def menu():
    inv = Inventario("inventario.txt")

    while True:
        print("=== SISTEMA DE INVENTARIO ===")
        print("1) Agregar producto")
        print("2) Actualizar producto")
        print("3) Eliminar producto")
        print("4) Listar productos")
        print("5) Buscar producto por código")
        print("6) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = pedir_int("Cantidad: ")
            precio = pedir_float("Precio: ")
            inv.agregar_producto(codigo, nombre, cantidad, precio)

        elif opcion == "2":
            codigo = input("Código del producto a actualizar: ").strip()
            print("Deja vacío si no quieres cambiar un campo.")
            nombre = input("Nuevo nombre: ").strip()
            cantidad_txt = input("Nueva cantidad: ").strip()
            precio_txt = input("Nuevo precio: ").strip()

            nombre_val = nombre if nombre != "" else None
            cantidad_val = int(cantidad_txt) if cantidad_txt != "" else None
            precio_val = float(precio_txt) if precio_txt != "" else None

            inv.actualizar_producto(codigo, nombre=nombre_val, cantidad=cantidad_val, precio=precio_val)

        elif opcion == "3":
            codigo = input("Código del producto a eliminar: ").strip()
            inv.eliminar_producto(codigo)

        elif opcion == "4":
            inv.listar_productos()

        elif opcion == "5":
            codigo = input("Código a buscar: ").strip()
            inv.buscar_producto(codigo)

        elif opcion == "6":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu()