import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# ========================
# FUNCIÓN: AGREGAR EVENTO
# ========================
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Error", "Completa todos los campos")
        return

    # Insertar en la tabla
    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar campos
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)

# ========================
# FUNCIÓN: ELIMINAR EVENTO
# ========================
def eliminar_evento():
    seleccionado = tree.selection()

    if not seleccionado:
        messagebox.showwarning("Error", "Selecciona un evento")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento?")

    if confirmar:
        tree.delete(seleccionado)

# ========================
# VENTANA PRINCIPAL
# ========================
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("650x450")

# ========================
# FRAME LISTA (TABLA)
# ========================
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show="headings")

tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripcion", text="Descripción")

tree.pack()

# ========================
# FRAME FORMULARIO
# ========================
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

# FECHA
tk.Label(frame_form, text="Fecha:").grid(row=0, column=0)
entrada_fecha = DateEntry(frame_form)
entrada_fecha.grid(row=0, column=1)

# HORA
tk.Label(frame_form, text="Hora:").grid(row=1, column=0)
entrada_hora = tk.Entry(frame_form)
entrada_hora.insert(0, "14:30")  # ejemplo real
entrada_hora.grid(row=1, column=1)

# DESCRIPCIÓN
tk.Label(frame_form, text="Descripción:").grid(row=2, column=0)
entrada_descripcion = tk.Entry(frame_form)
entrada_descripcion.insert(0, "Reunión con equipo")  # ejemplo real
entrada_descripcion.grid(row=2, column=1)

# ========================
# FRAME BOTONES
# ========================
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=5)

btn_salir = tk.Button(frame_botones, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=5)

# ========================
# EJEMPLO AUTOMÁTICO (DATOS REALES)
# ========================
tree.insert("", "end", values=("2026-03-22", "10:00", "Clase de programación"))
tree.insert("", "end", values=("2026-03-23", "16:00", "Entrenamiento"))
tree.insert("", "end", values=("2026-03-24", "09:30", "Reunión académica"))

# ========================
# INICIAR APP
# ========================
root.mainloop()
