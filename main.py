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


def login_cliente():
    ventana.destroy()
    ventana_login = tk.Toplevel(window)
    ventana_login.title("Login Cliente")
    ventana_login.geometry("400x250")
    ventana_login.resizable(False, False)
    ventana_login.transient(window)
    ventana_login.grab_set()

    tk.Label(ventana_login, text="Iniciar Sesión como Cliente",
             font=("Helvetica", 14, "bold")).pack(pady=20)

    tk.Label(ventana_login, text="Nombre:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana_login, width=30)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana_login, text="Celular:").pack(pady=5)
    entrada_celular = tk.Entry(ventana_login, width=30)
    entrada_celular.pack(pady=5)

    def validar_cliente():
        nombre = entrada_nombre.get().strip()
        celular = entrada_celular.get().strip()

        # Verificar si el cliente está registrado
        cliente_encontrado = None
        for cliente in CLIENTES_REGISTRADOS:
            if cliente['nombre'] == nombre and cliente['celular'] == celular:
                cliente_encontrado = cliente
                break

        if cliente_encontrado:
            messagebox.showinfo(f"¡Bienvenido {nombre}!")
            ventana_login.destroy()
            panel_cliente(nombre)
        else:
            messagebox.showerror("Error", "Cliente no registrado. Por favor regístrate primero.")

    tk.Button(ventana_login, text="Ingresar", command=validar_cliente,
              bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"),
              width=15, height=2).pack(pady=15)


btn_frame = tk.Frame(ventana)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Instructor", command=login_instructor,
          bg="#2196F3", fg="white", font=("Helvetica", 11, "bold"),
          width=12, height=2).pack(side=tk.LEFT, padx=10)

tk.Button(btn_frame, text="Cliente", command=login_cliente,
          bg="#FF9800", fg="white", font=("Helvetica", 11, "bold"),
          width=12, height=2).pack(side=tk.LEFT, padx=10)
