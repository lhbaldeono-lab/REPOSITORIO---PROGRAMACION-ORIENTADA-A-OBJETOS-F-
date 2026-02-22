# Sistema de Gestión de Inventarios Mejorado (Python)

## Descripción
Sistema en consola que permite administrar un inventario de productos (agregar, actualizar, eliminar, listar, buscar) y guarda automáticamente los cambios en un archivo de texto `inventario.txt`.

## Formato del archivo
Cada línea representa un producto:
codigo|nombre|cantidad|precio

Ejemplo:
A001|Arroz|20|1.25

## Manejo de errores
- Si `inventario.txt` no existe, el programa lo crea automáticamente.
- Maneja errores comunes:
  - FileNotFoundError (archivo inexistente)
  - PermissionError (sin permisos de lectura/escritura)
  - Líneas corruptas (se ignoran y se notifica)

## Ejecución
1. Abrir terminal en la carpeta del proyecto
2. Ejecutar:
   python main.py
