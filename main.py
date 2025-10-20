print("INTERFACES GENERALES")
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import io
import base64

class GymApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DAC PILATES")
        self.window.geometry("800x600")
        self.window.configure(bg="#d9b59c")

        self.usuario_actual = None
        self.celular_actual = None

        self.clases_registradas = {}
        self.mostrar_login()
    def crear_imagen(self,ancho, alto, color="#16213e"):
        img = Image.new("RGB", (ancho, alto), color)
        return ImageTk.PhotoImage(img)

    def mostrar_login(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.geometry("800x600")

        main_frame = tk.Frame(self.window, bg="#d9b59c")
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, bg="#d9b59c")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=40, pady=40)

        right_frame = tk.Frame(main_frame, bg="#d9b59c")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tk.Label(
            left_frame,
            text= "DAC PILATES",
            font= ("Helvetica", 28, "bold"),
            bg="#B77D55",
            fg="#000000"
        ).pack(pady=(20,10))

        tk.Label(
            left_frame,
            text= "Bienvenido",
            font= ("Helvetica", 16),
            bg="#B77D55",
            fg="#000000"
        ).pack(pady=(0,40))

        tk.Label(
            left_frame,
            text= "Nombre completo",
            font= ("Helvetica", 12),
            bg="#B77D55",
            fg="#000000"
        ).pack(anchor=tk.W, pady=(10,5))

        self.nombre = tk.Entry(
            left_frame,
            font= ("Helvetica", 14),
            bg="#B77D55",
            fg="#000000",
            insertbackground="#00d4ff",
            relief=tk.FLAT,
            bd=0
        )
        self.nombre.pack(fill=tk.X, ipady=10, pady=(0,20))

        tk.Label(
            left_frame,
            text= "Numero de celular",
            font= ("Helvetica", 12),
            bg="#B77D55",
            fg="#000000"
        ). pack(anchor=tk.W, pady=(10,5))

        self.celular = tk.Entry(
            left_frame,
            font= ("Helvetica", 14),
            bg="#B77D55",
            fg="#000000",
        )
        self.celular.pack(fill=tk.X, ipady=10, pady=(0,40))

        boton_ingreso= tk.Button(
            left_frame,
            text="Ingresar",
            font= ("Helvetica", 14, "bold"),
            bg="#B77D55",
            fg="#000000",
            activebackground="#00d4ff",
            activeforeground="#B77D55",
            relief= tk.FLAT,
            cursor= "hand2",
            command=self.validar_login
        )
        boton_ingreso.pack(fill=tk.X, ipady=12)

        def enter(e):
            boton_ingreso.config(bg="#B77D55")

        def leave(e):
            boton_ingreso.config(bg="#000000")

        boton_ingreso.bind("<Enter>", enter)
        boton_ingreso.bind("<Leave>", leave)

    def validar_login(self):
        nombre = self.nombre.get().strip()
        celular = self.celular.get().strip()

        if not nombre or not celular:
            messagebox.showerror("Error", "Completa todos los campos")
            return
        if not celular.isdigit() or len(celular) <8:
            messagebox.showerror("Error", "Debe ingresar 8 digitos")
            return

        self.usuario_actual = nombre
        self.celular_actual = celular
        self.mostrar_menu()


    def mostrar_menu(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.geometry("900x650")

        main_frame = tk.Frame(self.window, bg="#d9b59c")
        main_frame.pack(fill=tk.BOTH, expand=True)

        encabezado = tk.Frame(main_frame, bg="#d9b59c", height=100)
        encabezado.pack(fill=tk.X)
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text= "DAC PILATES",
            font= ("Helvetica", 24, "bold"),
            bg="#B77D55",
            fg="#000000"
        ).pack(side=tk.LEFT, padx=30, pady=20)

        tk.Label(
            encabezado,
            text= f"Bienvenido! {self.usuario_actual}",
            font= ("Helvetica", 14),
            bg="#B77D55",
        ).pack(side=tk.RIGHT,padx=30)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GymApp()
    app.run()