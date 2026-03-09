# ============================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ============================================
# Este archivo contiene las clases principales
# del sistema: Libro, Usuario y Biblioteca.
# Se aplican estructuras de datos de Python
# como tuplas, listas, diccionarios y conjuntos.
# ============================================


# --------------------------------------------
# Clase Libro
# Representa un libro dentro de la biblioteca
# --------------------------------------------
class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # Tupla para almacenar información inmutable
        self.info = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True


    def mostrar_info(self):

        return f"Título: {self.info[0]} | Autor: {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# --------------------------------------------
# Clase Usuario
# Representa un usuario registrado
# --------------------------------------------
class Usuario:

    def __init__(self, nombre, id_usuario):

        self.nombre = nombre
        self.id_usuario = id_usuario

        # Lista para almacenar libros prestados
        self.libros_prestados = []


    def prestar_libro(self, isbn):

        self.libros_prestados.append(isbn)


    def devolver_libro(self, isbn):

        if isbn in self.libros_prestados:
            self.libros_prestados.remove(isbn)


    def listar_libros(self):

        return self.libros_prestados


# --------------------------------------------
# Clase Biblioteca
# Gestiona libros, usuarios y préstamos
# --------------------------------------------
class Biblioteca:

    def __init__(self):

        # Diccionario para almacenar libros por ISBN
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para IDs únicos
        self.ids_usuarios = set()


    # ----------------------------------------
    # Añadir libro
    # ----------------------------------------
    def agregar_libro(self, libro):

        self.libros[libro.isbn] = libro
        print("Libro agregado correctamente")


    # ----------------------------------------
    # Eliminar libro
    # ----------------------------------------
    def eliminar_libro(self, isbn):

        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado del sistema")


    # ----------------------------------------
    # Registrar usuario
    # ----------------------------------------
    def registrar_usuario(self, usuario):

        if usuario.id_usuario not in self.ids_usuarios:

            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)

            print("Usuario registrado correctamente")


    # ----------------------------------------
    # Dar de baja usuario
    # ----------------------------------------
    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado del sistema")


    # ----------------------------------------
    # Prestar libro
    # ----------------------------------------
    def prestar_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro.disponible:

                libro.disponible = False
                usuario.prestar_libro(isbn)

                print("Libro prestado correctamente")

            else:

                print("El libro no está disponible")


    # ----------------------------------------
    # Devolver libro
    # ----------------------------------------
    def devolver_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            libro.disponible = True
            usuario.devolver_libro(isbn)

            print("Libro devuelto correctamente")


    # ----------------------------------------
    # Buscar libros
    # ----------------------------------------
    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():

            if titulo.lower() in libro.info[0].lower():
                print(libro.mostrar_info())


    def buscar_por_autor(self, autor):

        for libro in self.libros.values():

            if autor.lower() in libro.info[1].lower():
                print(libro.mostrar_info())


    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():

            if categoria.lower() == libro.categoria.lower():
                print(libro.mostrar_info())