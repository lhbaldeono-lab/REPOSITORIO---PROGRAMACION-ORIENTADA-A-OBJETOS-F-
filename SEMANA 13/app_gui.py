import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Lista de Datos")
ventana.geometry("400x350")

# ----------------------
# FUNCIONES
# ----------------------

def agregar_dato():
    dato = entrada.get()

    if dato != "":
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)


def limpiar_lista():
    lista.delete(0, tk.END)


# ----------------------
# COMPONENTES
# ----------------------

label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=10)

entrada = tk.Entry(ventana, width=30)
entrada.pack()

boton_agregar = tk.Button(
    ventana,
    text="Agregar",
    command=agregar_dato
)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(
    ventana,
    text="Limpiar",
    command=limpiar_lista
)
boton_limpiar.pack(pady=5)

label_lista = tk.Label(ventana, text="Lista de datos:")
label_lista.pack(pady=10)

lista = tk.Listbox(ventana, width=40, height=10)
lista.pack()

ventana.mainloop()