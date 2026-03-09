# ============================================
# SISTEMA DE BIBLIOTECA DIGITAL
# ============================================


# --------------------------------------------
# Clase Libro
# --------------------------------------------
class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # tupla (dato inmutable)
        self.info = (titulo, autor)

        self.categoria = categoria
        self.isbn = isbn
        self.disponible = True


    def mostrar_info(self):

        return f"Título: {self.info[0]} | Autor: {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"


# --------------------------------------------
# Clase Usuario
# --------------------------------------------
class Usuario:

    def __init__(self, nombre, id_usuario):

        self.nombre = nombre
        self.id_usuario = id_usuario

        # lista
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
# --------------------------------------------
class Biblioteca:

    def __init__(self):

        # diccionario
        self.libros = {}

        self.usuarios = {}

        # set
        self.ids_usuarios = set()


    def agregar_libro(self, libro):

        self.libros[libro.isbn] = libro
        print("Libro agregado correctamente")


    def registrar_usuario(self, usuario):

        if usuario.id_usuario not in self.ids_usuarios:

            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)

            print("Usuario registrado correctamente")


    def prestar_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            if libro.disponible:

                libro.disponible = False
                usuario.prestar_libro(isbn)

                print("Libro prestado correctamente")


    def devolver_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            libro.disponible = True
            usuario.devolver_libro(isbn)

            print("Libro devuelto correctamente")


    def buscar_por_autor(self, autor):

        for libro in self.libros.values():

            if autor.lower() in libro.info[1].lower():
                print(libro.mostrar_info())


    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():

            if categoria.lower() == libro.categoria.lower():
                print(libro.mostrar_info())


# ============================================
# PRUEBA DEL SISTEMA
# ============================================

biblioteca = Biblioteca()


libro1 = Libro("Clean Code", "Robert C. Martin", "Programación", "ISBN001")
libro2 = Libro("Automate the Boring Stuff with Python", "Al Sweigart", "Programación", "ISBN002")
libro3 = Libro("The Pragmatic Programmer", "Andrew Hunt", "Programación", "ISBN003")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)


usuario1 = Usuario("Juan Carlos Perez", "U001")

biblioteca.registrar_usuario(usuario1)


biblioteca.prestar_libro("ISBN001", "U001")


print("\nLibros prestados al usuario:")
print(usuario1.listar_libros())


biblioteca.devolver_libro("ISBN001", "U001")


print("\nBuscar por autor:")
biblioteca.buscar_por_autor("Robert")

print("\nBuscar por categoría:")
biblioteca.buscar_por_categoria("Programación")