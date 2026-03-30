import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tareas = []

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.agregar_tarea)

        # Botones
        tk.Button(root, text="Añadir Tarea", command=self.agregar_tarea).pack()
        tk.Button(root, text="Completar", command=self.completar_tarea).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar_tarea).pack()

        # Lista
        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

    def agregar_tarea(self, event=None):
        texto = self.entry.get()
        if texto != "":
            self.tareas.append({"texto": texto, "completada": False})
            self.entry.delete(0, tk.END)
            self.actualizar_lista()

    def completar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            i = seleccion[0]
            self.tareas[i]["completada"] = True
            self.actualizar_lista()

    def eliminar_tarea(self):
        seleccion = self.listbox.curselection()
        if seleccion:
            i = seleccion[0]
            self.tareas.pop(i)
            self.actualizar_lista()

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = "✔ " + texto
            self.listbox.insert(tk.END, texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
