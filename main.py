import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

CLASES = []  # Lista de clases disponibles
CLIENTES_REGISTRADOS = []  # Lista de clientes registrados
INSCRIPCIONES = {}  # {cliente_nombre: [lista de clases]}

def ventana_iniciar_sesion():
    ventana = tk.Toplevel(window)
    ventana.title("Iniciar Sesión")
    ventana.geometry("400x250")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()
    tk.Label(ventana, text="¿Cómo deseas iniciar sesión?",
             font=("Helvetica", 12, "bold")).pack(pady=30)

    def login_instructor():
        INSTRUCTOR_NOMBRE = "Fabiola Acevez"
        INSTRUCTOR_CELULAR = "45348967"

        ventana.destroy()
        ventana_login = tk.Toplevel(window)
        ventana_login.title("Login Instructor")
        ventana_login.geometry("400x250")
        ventana_login.resizable(False, False)
        ventana_login.transient(window)
        ventana_login.grab_set()

        tk.Label(ventana_login, text="Iniciar Sesión como instructor",
                 font=("Helvetica", 14, "bold")).pack(pady=20)

        tk.Label(ventana_login, text="Nombre:").pack(pady=5)
        entrada_nombre = tk.Entry(ventana_login, width=30)
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_login, text="Celular:").pack(pady=5)
        entrada_celular = tk.Entry(ventana_login, width=30)
        entrada_celular.pack(pady=5)

        def validar_instructor():
            if (entrada_nombre.get() == INSTRUCTOR_NOMBRE and
                    entrada_celular.get() == INSTRUCTOR_CELULAR):
                messagebox.showinfo("Éxito", f"¡Bienvenido Instructor {INSTRUCTOR_NOMBRE}!")
                ventana_login.destroy()
                panel_instructor()
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")

        tk.Button(ventana_login, text="Ingresar", command=validar_instructor,
                  bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
                  width=15, height=2).pack(pady=15)
