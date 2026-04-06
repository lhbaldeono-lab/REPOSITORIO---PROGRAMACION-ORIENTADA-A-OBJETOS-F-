import tkinter as tk

# ---------- FUNCIONES ----------
def agregar_tarea(event=None):
    tarea = entrada.get().strip()
    if tarea != "":
        lista.insert(tk.END, tarea)
        entrada.delete(0, tk.END)

def marcar_completada(event=None):
    try:
        indice = lista.curselection()[0]
        texto = lista.get(indice)

        if not texto.startswith("✔ "):
            lista.delete(indice)
            lista.insert(indice, "✔ " + texto)
            lista.itemconfig(indice, fg="gray")
    except:
        pass

def eliminar_tarea(event=None):
    try:
        indice = lista.curselection()[0]
        lista.delete(indice)
    except:
        pass

def cerrar_app(event=None):
    ventana.destroy()

# ---------- INTERFAZ ----------
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(ventana, text="Marcar Completada", command=marcar_completada)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
lista = tk.Listbox(ventana, width=40, height=10, selectbackground="lightblue")
lista.pack(pady=10)

# ---------- ATAJOS ----------
ventana.bind("<Return>", agregar_tarea)     # Enter
ventana.bind("c", marcar_completada)        # tecla C
ventana.bind("<Delete>", eliminar_tarea)    # Delete
ventana.bind("<Escape>", cerrar_app)        # ESC

# ---------- LOOP ----------
ventana.mainloop()