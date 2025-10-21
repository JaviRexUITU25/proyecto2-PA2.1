print("INTERFACES GENERALES")
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
#CLASE UNICA
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

    def crear_imagen(self, ancho, alto, color="#16213e"):
        img = Image.new("RGB", (ancho, alto), color)
        return ImageTk.PhotoImage(img)

#VENTANA
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
        try:
            imagen_empresa = Image.open("Dac logo png.png")
            imagen_empresa = imagen_empresa.resize((400,400))
            self.foto_empresa = ImageTk.PhotoImage(imagen_empresa)
            label_imagen = tk.Label(right_frame, image=self.foto_empresa, bg="#d9b59c")
            label_imagen.pack(expand=True)
        except:
            pass

        tk.Label(
            left_frame,
            text="DAC PILATES",
            font=("Helvetica", 28, "bold"),
            bg="#d9b59c",
            fg="#000000"
        ).pack(pady=(20, 10))

        tk.Label(
            left_frame,
            text="Bienvenido",
            font=("Helvetica", 16),
            bg="#d9b59c",
            fg="#000000"
        ).pack(pady=(0, 40))

#etiqueta para agregar tu nombre
        tk.Label(
            left_frame,
            text="Nombre completo",
            font=("Helvetica", 12),
            bg="#d9b59c",
            fg="#000000"
        ).pack(anchor=tk.W, pady=(10, 5))

        self.nombre = tk.Entry(
            left_frame,
            font=("Helvetica", 14),
            bg="#B77D55",
            fg="#000000",
            insertbackground="#00d4ff",
            relief=tk.FLAT,
            bd=0
        )
        self.nombre.pack(fill=tk.X, ipady=10, pady=(0, 20))

#etiqueta para agregar tu numero celular
        tk.Label(
            left_frame,
            text="Numero de celular (deben ser 8 dígitos)",
            font=("Helvetica", 12),
            bg="#d9b59c",
            fg="#000000"
        ).pack(anchor=tk.W, pady=(10, 5))

        self.celular = tk.Entry(
            left_frame,
            font=("Helvetica", 14),
            bg="#B77D55",
            fg="#000000",
        )
        self.celular.pack(fill=tk.X, ipady=10, pady=(0, 40))

        boton_ingresoINS = tk.Button(
            left_frame,
            text= "Ingresar como instructor",
            font=("Helvetica", 14, "bold"),
            bg="#d9b59c",
            fg="#000000",
            activebackground="#d9b59c",
            activeforeground="#B77D55",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.validar_login
        )
        boton_ingresoINS.pack(fill=tk.X, ipady=12)


        boton_ingresoUS = tk.Button(
            left_frame,
            text="Ingresar",
            font=("Helvetica", 14, "bold"),
            bg="#d9b59c",
            fg="#000000",
            activebackground="#d9b59c",
            activeforeground="#B77D55",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.validar_login
        )
        boton_ingresoUS.pack(fill=tk.X, ipady=12)

#El color de fondo cuando el usuario pasa el cursor
        def enter(e):
            boton_ingreso.config(bg="#d9b59c")

        def leave(e):
            boton_ingreso.config(bg="#d9b59c")

        boton_ingresoUS.bind("<Enter>", enter)
        boton_ingresoUS.bind("<Leave>", leave)
        boton_ingresoINS.bind("<Enter>", enter)
        boton_ingresoINS.bind("<Leave>", leave)

    def validar_login(self):
        nombre = self.nombre.get().strip()
        celular = self.celular.get().strip()

        if not nombre or not celular:
            messagebox.showerror("Error", "Completa todos los campos")
            return
        if not celular.isdigit() or len(celular) < 8 or len(celular) >8:
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

#bg= color del fondo
#fg= color de la letra
        tk.Label(
            encabezado,
            text="DAC PILATES",
            font=("Helvetica", 24, "bold"),
            bg="#d9b59c",
            fg="#000000"
        ).pack(side=tk.LEFT, padx=30, pady=20)

        tk.Label(
            encabezado,
            text=f"Bienvenido! {self.usuario_actual}",
            font=("Helvetica", 14),
            bg="#d9b59c",
        ).pack(side=tk.RIGHT, padx=30)

        try:
            imagen_logo = Image.open("Dac logo png.png")
            imagen_logo =imagen_logo.resize((80,80))
            self.logo= ImageTk.PhotoImage(imagen_logo)

            label_logo = tk.Label(encabezado, image=self.logo, bg="#d9b59c")
            label_logo.pack(side=tk.LEFT, padx=20)
        except:
            pass

        content_frame = tk.Frame(main_frame, bg="#d9b59c")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=40)

        tk.Label(
            content_frame,
            text="Clases de pilates",
            font=("Helvetica", 29, "bold"),
            bg="#d9b59c",
            fg="#000000"
        ).pack(pady=(0, 30))

        frame_boton = tk.Frame(content_frame, bg="#d9b59c")
        frame_boton.pack(expand=True)

        self.crear_boton(
            frame_boton,
            "VER HORARIOS",
            "#d9b59c",
            "#00a8cc",
            self.mostrar_horarios
        ).pack(pady=15, ipadx=40, ipady=20)

        self.crear_boton(
            frame_boton,
            "UNIRSE A UNA CLASE",
            "#d9b59c",
            "#00a8cc",
            self.unirse_clase
        ).pack(pady=15, ipadx=40, ipady=20)

        self.crear_boton(
            frame_boton,
            "QUITAR REGISTRO",
            "#d9b59c",
            "#00a8cc",
            self.quitar_registro
        ).pack(pady=15, ipadx=40, ipady=20)

        boton_salir = tk.Button(
            content_frame,
            text="Cerrar Sesión",
            font=("Helvetica", 10),
            bg="#d9b59c",
            fg="#000000",
            activebackground="#d9b59c",
            activeforeground="#B77D55",
            relief=tk.FLAT,
            cursor="hand2",
            command=self.mostrar_login
        )
        boton_salir.pack(side=tk.BOTTOM, ipady=20)

    def crear_boton(self, parent, texto, color, color_hover, comando):
        boton = tk.Button(
            parent,
            text=texto,
            font=("Helvetica", 16, "bold"),
            bg=color,
            fg="#000000",
            activebackground=color_hover,
            activeforeground="#000000",
            relief=tk.FLAT,
            cursor="hand2",
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

    def unirse_clase(self):
        ventana = tk.Toplevel(self.window)
        ventana.title("Unirse a Clase")
        ventana.geometry("400x350")
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
            "Martes 9:00 am - 10:00 am",
            "Martes 10:20 am - 11:20 am",
            "Martes 6:00 pm - 7:00 pm",
            "Martes 8:00 pm - 9:00 pm",
            "Jueves 9:00 am - 10:00 am",
            "Jueves 10:20 am - 11:20 am",
            "Jueves 6:00 pm - 7:00 pm",
            "Jueves 8:00 pm - 9:00 pm",
            "Viernes 9:00 am - 10:00 am",
            "Viernes 10:20 am - 11:20 am",
            "Viernes 6:00 pm - 7:00 pm",
            "Viernes 8:00 pm - 9:00 pm",
            "Miercoles 9:00 am - 10:00 am",
            "Miercoles 6:00 pm - 7:00 pm",
            "Miercoles 8:00 pm - 9:00 pm",
            "Martes 6:00 am - 7:00 am",
            "Miercoles 6:00 am - 7:00 am",
            "Jueves 6:00 am - 7:00 am",
        ]

        combo = ttk.Combobox(ventana, values=horarios, font=("Helvetica", 12), width=25)
        combo.pack(pady=20)

        def registrar():
            horario_seleccionado = combo.get()
            if not horario_seleccionado:
                messagebox.showerror("Error", "Selecciona un horario")
                return

            # Verificar si ya está registrado en esta clase
            if horario_seleccionado in self.clases_registradas.get(self.celular_actual, []):
                messagebox.showwarning("Advertencia", "Ya estás registrado en esta clase")
                return

            # Registrar la clase
            if self.celular_actual not in self.clases_registradas:
                self.clases_registradas[self.celular_actual] = []

            self.clases_registradas[self.celular_actual].append(horario_seleccionado)
            messagebox.showinfo("Éxito", f"Te has registrado en:\n{horario_seleccionado}")
            ventana.destroy()

        boton_registrar = tk.Button(
            ventana,
            text="Registrar",
            font=("Helvetica", 14, "bold"),
            bg="#00d4ff",
            fg="#000000",
            activebackground="#00a8cc",
            relief=tk.FLAT,
            cursor="hand2",
            command=registrar
        )
        boton_registrar.pack(pady=20, ipadx=30, ipady=10)

    def quitar_registro(self):
        if self.celular_actual not in self.clases_registradas or not self.clases_registradas[self.celular_actual]:
            messagebox.showinfo("Información", "No tienes clases registradas")
            return

        ventana = tk.Toplevel(self.window)
        ventana.title("Quitar Registro")
        ventana.geometry("400x350")
        ventana.configure(bg="#B77D55")

        tk.Label(
            ventana,
            text="Selecciona la clase a quitar",
            font=("Helvetica", 16, "bold"),
            bg="#B77D55",
            fg="#000000"
        ).pack(pady=20)

        clases_usuario = self.clases_registradas[self.celular_actual]

        combo = ttk.Combobox(ventana, values=clases_usuario, font=("Helvetica", 12), width=25)
        combo.pack(pady=20)

        def quitar():
            clase_seleccionada = combo.get()
            if not clase_seleccionada:
                messagebox.showerror("Error", "Selecciona una clase")
                return

            self.clases_registradas[self.celular_actual].remove(clase_seleccionada)
            messagebox.showinfo("Éxito", f"Has salido de:\n{clase_seleccionada}")
            ventana.destroy()

        boton_quitar = tk.Button(
            ventana,
            text="Quitar Registro",
            font=("Helvetica", 14, "bold"),
            bg="#ff4444",
            fg="#000000",
            activebackground="#cc0000",
            relief=tk.FLAT,
            cursor="hand2",
            command=quitar
        )
        boton_quitar.pack(pady=20, ipadx=30, ipady=10)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = GymApp()
    app.run()