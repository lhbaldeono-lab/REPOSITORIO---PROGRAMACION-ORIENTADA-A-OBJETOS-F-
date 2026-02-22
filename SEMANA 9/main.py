# Sistema de Gestión de Inventarios (POO) - Versión Simple
# Requisitos cumplidos:
# - Clase Producto con ID único, nombre, cantidad, precio
# - Constructor + getters y setters
# - Clase Inventario con lista de productos y métodos:
#   agregar (ID único), eliminar por ID, actualizar, buscar por nombre, mostrar todos
# - Menú interactivo en consola

class Producto:
    def __init__(self, producto_id: str, nombre: str, cantidad: int, precio: float):
        self.__id = producto_id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_nombre(self, nuevo_nombre: str) -> None:
        self.__nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad: int) -> None:
        self.__cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float) -> None:
        self.__precio = nuevo_precio

    def __str__(self) -> str:
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio:.2f}"


class Inventario:
    def __init__(self):
        self.productos = []  # Lista de objetos Producto

    def id_existe(self, producto_id: str) -> bool:
        for p in self.productos:
            if p.get_id() == producto_id:
                return True
        return False

    def agregar_producto(self, producto: Producto) -> bool:
        if self.id_existe(producto.get_id()):
            return False
        self.productos.append(producto)
        return True

    def eliminar_producto_por_id(self, producto_id: str) -> bool:
        for i, p in enumerate(self.productos):
            if p.get_id() == producto_id:
                del self.productos[i]
                return True
        return False

    def actualizar_por_id(self, producto_id: str, nueva_cantidad=None, nuevo_precio=None) -> bool:
        for p in self.productos:
            if p.get_id() == producto_id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                return True
        return False

    def buscar_por_nombre(self, texto: str):
        texto = texto.lower()
        resultados = []
        for p in self.productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_todos(self) -> None:
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n--- INVENTARIO ---")
        for p in self.productos:
            print(p)
        print("------------------\n")


def pedir_int(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("❌ No se permiten valores negativos.")
                continue
            return valor
        except ValueError:
            print("❌ Debes ingresar un número entero.")


def pedir_float(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("❌ No se permiten valores negativos.")
                continue
            return valor
        except ValueError:
            print("❌ Debes ingresar un número (ej: 2.50).")


def menu():
    inv = Inventario()

    while True:
        print("=== SISTEMA DE GESTIÓN DE INVENTARIOS ===")
        print("1) Añadir producto")
        print("2) Eliminar producto por ID")
        print("3) Actualizar cantidad o precio por ID")
        print("4) Buscar producto(s) por nombre")
        print("5) Mostrar todos los productos")
        print("6) Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            producto_id = input("ID (único): ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = pedir_int("Cantidad: ")
            precio = pedir_float("Precio: ")

            nuevo = Producto(producto_id, nombre, cantidad, precio)
            if inv.agregar_producto(nuevo):
                print("✅ Producto añadido correctamente.")
            else:
                print("❌ Error: ese ID ya existe. Debe ser único.")

        elif opcion == "2":
            producto_id = input("ID del producto a eliminar: ").strip()
            if inv.eliminar_producto_por_id(producto_id):
                print("✅ Producto eliminado.")
            else:
                print("❌ No se encontró un producto con ese ID.")

        elif opcion == "3":
            producto_id = input("ID del producto a actualizar: ").strip()
            print("Deja vacío lo que NO quieras cambiar.")
            cantidad_txt = input("Nueva cantidad: ").strip()
            precio_txt = input("Nuevo precio: ").strip()

            nueva_cantidad = int(cantidad_txt) if cantidad_txt != "" else None
            nuevo_precio = float(precio_txt) if precio_txt != "" else None

            if nueva_cantidad is None and nuevo_precio is None:
                print("⚠️ No cambiaste nada.")
                continue

            if inv.actualizar_por_id(producto_id, nueva_cantidad, nuevo_precio):
                print("✅ Producto actualizado.")
            else:
                print("❌ No se encontró un producto con ese ID.")

        elif opcion == "4":
            texto = input("Escribe el nombre o parte del nombre a buscar: ").strip()
            resultados = inv.buscar_por_nombre(texto)
            if resultados:
                print("\n✅ Resultados encontrados:")
                for p in resultados:
                    print(p)
                print()
            else:
                print("❌ No se encontraron productos con ese nombre.")

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "6":
            print("👋 Saliendo...")
            break

        else:
            print("❌ Opción inválida. Intenta otra vez.")


menu()