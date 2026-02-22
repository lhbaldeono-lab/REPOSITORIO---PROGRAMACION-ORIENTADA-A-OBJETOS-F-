# inventario.py
# Sistema de Gestión de Inventarios Mejorado
# - Guarda en archivo (inventario.txt)
# - Carga automáticamente al iniciar
# - Maneja excepciones (FileNotFoundError, PermissionError, datos corruptos)

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Producto:
    codigo: str
    nombre: str
    cantidad: int
    precio: float

    def to_line(self) -> str:
        # Formato del archivo: codigo|nombre|cantidad|precio
        return f"{self.codigo}|{self.nombre}|{self.cantidad}|{self.precio}"

    @staticmethod
    def from_line(line: str) -> Optional["Producto"]:
        """
        Convierte una línea del archivo a un Producto.
        Si la línea está corrupta o no cumple formato, devuelve None.
        """
        parts = line.strip().split("|")
        if len(parts) != 4:
            return None

        codigo, nombre, cantidad_str, precio_str = parts
        try:
            cantidad = int(cantidad_str)
            precio = float(precio_str)
            if cantidad < 0 or precio < 0:
                return None
            return Producto(codigo=codigo, nombre=nombre, cantidad=cantidad, precio=precio)
        except ValueError:
            return None


class Inventario:
    def __init__(self, archivo: str = "inventario.txt"):
        self.archivo = archivo
        self.productos: Dict[str, Producto] = {}
        # Al iniciar, intenta cargar productos del archivo
        self.cargar_desde_archivo()

    # ----------------------------
    # MANEJO DE ARCHIVOS
    # ----------------------------
    def cargar_desde_archivo(self) -> None:
        """
        Carga el inventario desde el archivo.
        - Si no existe, lo crea vacío.
        - Si hay líneas corruptas, las ignora y avisa.
        """
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                lineas = f.readlines()

            corruptas = 0
            for linea in lineas:
                if not linea.strip():
                    continue
                prod = Producto.from_line(linea)
                if prod is None:
                    corruptas += 1
                    continue
                self.productos[prod.codigo] = prod

            if corruptas > 0:
                print(f"⚠️ Aviso: se ignoraron {corruptas} línea(s) corrupta(s) en {self.archivo}.")

        except FileNotFoundError:
            # Si no existe, lo creamos
            try:
                with open(self.archivo, "w", encoding="utf-8") as _:
                    pass
                print(f"📄 No existía {self.archivo}. Se creó un archivo nuevo.")
            except PermissionError:
                print(f"❌ Error: No tienes permisos para crear {self.archivo}.")
        except PermissionError:
            print(f"❌ Error: No tienes permisos para leer {self.archivo}.")

    def guardar_en_archivo(self) -> bool:
        """
        Guarda TODO el inventario en el archivo (reescribe el archivo).
        Devuelve True si guardó, False si falló.
        """
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for producto in self.productos.values():
                    f.write(producto.to_line() + "\n")
            return True
        except PermissionError:
            print(f"❌ Error: No tienes permisos para escribir en {self.archivo}.")
            return False
        except OSError as e:
            print(f"❌ Error inesperado al escribir archivo: {e}")
            return False

    # ----------------------------
    # OPERACIONES DEL INVENTARIO
    # ----------------------------
    def agregar_producto(self, codigo: str, nombre: str, cantidad: int, precio: float) -> bool:
        if codigo in self.productos:
            print("❌ Ya existe un producto con ese código.")
            return False
        if cantidad < 0 or precio < 0:
            print("❌ Cantidad y precio no pueden ser negativos.")
            return False

        self.productos[codigo] = Producto(codigo, nombre, cantidad, precio)
        ok = self.guardar_en_archivo()

        if ok:
            print("✅ Producto agregado y guardado en el archivo.")
            return True
        else:
            # Si falló guardar, revertimos para no mentirle al usuario
            del self.productos[codigo]
            print("❌ No se pudo guardar en el archivo. Operación revertida.")
            return False

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                            cantidad: Optional[int] = None, precio: Optional[float] = None) -> bool:
        if codigo not in self.productos:
            print("❌ No existe un producto con ese código.")
            return False

        producto_original = self.productos[codigo]

        # Copia de seguridad por si falla el guardado
        backup = Producto(
            codigo=producto_original.codigo,
            nombre=producto_original.nombre,
            cantidad=producto_original.cantidad,
            precio=producto_original.precio
        )

        if nombre is not None and nombre.strip() != "":
            producto_original.nombre = nombre

        if cantidad is not None:
            if cantidad < 0:
                print("❌ La cantidad no puede ser negativa.")
                return False
            producto_original.cantidad = cantidad

        if precio is not None:
            if precio < 0:
                print("❌ El precio no puede ser negativo.")
                return False
            producto_original.precio = precio

        ok = self.guardar_en_archivo()
        if ok:
            print("✅ Producto actualizado y guardado en el archivo.")
            return True
        else:
            # Revertimos cambios
            self.productos[codigo] = backup
            print("❌ No se pudo guardar en el archivo. Cambios revertidos.")
            return False

    def eliminar_producto(self, codigo: str) -> bool:
        if codigo not in self.productos:
            print("❌ No existe un producto con ese código.")
            return False

        backup = self.productos[codigo]
        del self.productos[codigo]

        ok = self.guardar_en_archivo()
        if ok:
            print("✅ Producto eliminado y archivo actualizado.")
            return True
        else:
            # Revertimos eliminación
            self.productos[codigo] = backup
            print("❌ No se pudo guardar en el archivo. Eliminación revertida.")
            return False

    def listar_productos(self) -> None:
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n--- INVENTARIO ---")
        for p in self.productos.values():
            print(f"Código: {p.codigo} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")
        print("------------------\n")

    def buscar_producto(self, codigo: str) -> None:
        p = self.productos.get(codigo)
        if not p:
            print("❌ Producto no encontrado.")
            return
        print(f"✅ Encontrado: {p.codigo} | {p.nombre} | Cantidad: {p.cantidad} | Precio: ${p.precio:.2f}")
        