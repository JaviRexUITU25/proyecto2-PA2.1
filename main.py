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

        content_frame = tk.Frame(main_frame, bg="#d9b59c")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=40)

        tk.Label(
            content_frame,
            text= "Clases de pilates",
            font=("Helvetica", 29,"bold"),
            bg="#B77D55",
            fg="#000000"
        ).pack(pady=(0,30))

        frame_boton = tk.Frame(content_frame, bg="#d9b59c")
        frame_boton.pack(expand=True)

        self.crear_boton(
            frame_boton,
            "VER HORARIOS",
            "#00d4ff",
            "#00a8cc",
            self.mostrar_horarios
        ).pack(pady=15, iádx=40, ipady=20)

        self.crear_boton(
            frame_boton,
            "UNIRSE A UNA CLASE",
            "#00d4ff",
            "#00a8cc",
            self.uniser_clase
        ).pack(pady=15, ipadx=40, ipady=20)

        self.crear_boton(
            frame_boton,
            "QUITAR REGISTRO"
            "#00d4ff",
            "#00a8cc",
            self.quitar_registro
        ).pack(pady=15, ipadx=40, ipady=20)

        boton_salir = tk.Button(
            content_frame,
            text= "Cerrar Sesión",
            font= ("Helvetica", 10),
            bg="#B77D55",
            fg="#000000",
            activebackground="#00d4ff",
            activeforeground="#B77D55",
            relief= tk.FLAT,
            cursor= "hand2",
            command=self.mostrar_login
        )
        boton_salir.pack(side=tk.BOTTOM, ipady=20)
    def crear_boton(self,parent, texto, color, color_hover, comando):
        boton = tk.Button(
            parent,
            text=texto,
            font=("Helvetica", 16, "bold"),
            bg=color,
            fg="#000000",
            activebackground=color_hover,
            activeforeground="#000000",
            relief=tk.FLAT,
            cursor= "hand2",
            command=comando,
            width=25
        )

        def enter(e):
            boton.config(bg=color_hover)

        def leave(e):
            boton.config(bg=color)

        boton.bind("<Enter>", enter)
        boton.bind("<Leave>", leave)
        return boton

    def mostrar_horarios(self):
        horarios = """
        Lunes, Martes, Jueves y Viernes
        9:00 am - 10:00 am
        10:20 am - 11:20 am
        6:00 pm - 7:00 pm
        8:00 pm - 9:00 pm
        
        Miercoles
        9:00 am - 10:00 am
        6:00 pm - 7:00 pm
        8:00 pm - 9:00 pm
        
        Martes, Miercoles y Jueves
        6:00 am - 7:00 am
        """
        messagebox.showinfo("Horarios de Pilates", horarios)

    def uniser_clase(self):
        ventana = tk.Toplevel(self.window)
        ventana.little("Unirse a Clase")
        ventana.geometry("400x300")
        ventana.configure(bg="#B77D55")

        tk.Label(
            ventana,
            text="Selecciona un horario",
            font=("Helvetica", 16, "bold"),
            bg="#B77D55",
            fg="#000000"
        ).pack(pady=20)

        horarios = [
            "Lunes 9:00 am - 10:00 am",
            "Lunes 10:20 am - 11:20 am",
            "Lunes 6:00 pm - 7:00 pm",
            "Lunes 8:00 pm - 9:00 pm",
            "Martes 9:00 am - 10:00 am"
            "Martes 10:20 am - 11:20 am"
            "Martes 6:00 pm - 7:00 pm"
            "Martes 8:00 pm - 9:00 pm",
            "Jueves 9:00 am - 10:00 am"
            "Jueves 10:20 am - 11:20 am"
            "Jueves 6:00 pm - 7:00 pm"
            "Jueves 8:00 pm - 9:00 pm",
            "Viernes 9:00 am - 10:00 am"
            "Viernes 10:20 am - 11:20 am"
            "Viernes 6:00 pm - 7:00 pm"
            "Viernes 8:00 pm - 9:00 pm"
            "Miercoles 9:00 am - 10:00 am"
            "Miercoles 6:00 pm - 7:00 pm"
            "Miercoles 8:00 pm - 9:00 pm"
            "Martes 6:00 am - 7:00 am"
            "Miercoles 6:00 am - 7:00 am"
            "Jueves 6:00 am - 7:00 am",
        ]
        combo = ttk.Combobox(ventana, values=horarios, font=("Helvetica", 12), width=20)
        combo.pack(pady=20)


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GymApp()
    app.run()