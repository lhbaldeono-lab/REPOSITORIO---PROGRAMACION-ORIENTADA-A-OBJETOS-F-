# Tienda Virtual - Ejemplo de Programación Orientada a Objetos
# Autor: Luis Henry Baldeón Ochoa
# Descripción: Simulación de una tienda virtual utilizando POO.

class Producto:
    """
    Clase que representa un producto de la tienda.
    """
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_producto(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"


class CarritoCompras:
    """
    Clase que representa el carrito de compras.
    """
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def mostrar_carrito(self):
        for producto in self.productos:
            print(producto.mostrar_producto())
        print(f"Total a pagar: ${self.calcular_total()}")


# Creación de objetos
producto1 = Producto("Laptop", 850)
producto2 = Producto("Mouse", 25)

carrito = CarritoCompras()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

# Ejecución
carrito.mostrar_carrito()
