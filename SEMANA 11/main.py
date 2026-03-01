import json

# -----------------------------
# Clase Producto
# -----------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def set_precio(self, precio):
        if precio >= 0:
            self.precio = precio


# -----------------------------
# Clase Inventario
# -----------------------------
class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}

    def añadir_producto(self, producto):
        if producto.get_id() not in self.productos:
            self.productos[producto.get_id()] = producto
            return True
        return False

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id].set_precio(precio)
            return True
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if p.get_nombre().lower() == nombre.lower()]

    def mostrar_todos(self):
        return list(self.productos.values())

    def guardar_archivo(self, archivo):
        data = {}
        for id, producto in self.productos.items():
            data[id] = {
                "id": producto.get_id(),
                "nombre": producto.get_nombre(),
                "cantidad": producto.get_cantidad(),
                "precio": producto.get_precio()
            }
        with open(archivo, "w") as f:
            json.dump(data, f, indent=4)


# -----------------------------
# FUNCIÓN PARA CARGAR FRUTAS INICIALES
# -----------------------------
def cargar_frutas_iniciales(inventario):
    frutas = [
        Producto("FR001", "Manzana", 50, 0.50),
        Producto("FR002", "Banano", 100, 0.30),
        Producto("FR003", "Naranja", 80, 0.40),
        Producto("FR004", "Fresa", 60, 1.20),
        Producto("FR005", "Mango", 40, 0.90),
        Producto("FR006", "Piña", 25, 1.50),
        Producto("FR007", "Uva", 70, 2.00)
    ]

    for fruta in frutas:
        inventario.añadir_producto(fruta)


# -----------------------------
# MENÚ
# -----------------------------
def menu():
    inventario = Inventario()
    cargar_frutas_iniciales(inventario)  # ← aquí se cargan las frutas

    while True:
        print("\n--- SISTEMA DE INVENTARIO DE FRUTAS ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos")
        print("6. Guardar y salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id, nombre, cantidad, precio)
            if inventario.añadir_producto(producto):
                print("Producto añadido correctamente.")
            else:
                print("El ID ya existe.")

        elif opcion == "2":
            id = input("ID a eliminar: ")
            if inventario.eliminar_producto(id):
                print("Producto eliminado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "3":
            id = input("ID a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            if inventario.actualizar_producto(id, cantidad, precio):
                print("Producto actualizado.")
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            for p in resultados:
                print(p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio())
            if not resultados:
                print("No encontrado.")

        elif opcion == "5":
            productos = inventario.mostrar_todos()
            for p in productos:
                print(p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio())
            if not productos:
                print("Inventario vacío.")

        elif opcion == "6":
            inventario.guardar_archivo("inventario.json")
            print("Inventario guardado. Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()