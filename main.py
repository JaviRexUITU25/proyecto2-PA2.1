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


def panel_instructor():
    ventana = tk.Toplevel(window)
    ventana.title("Panel de Instructor")
    ventana.geometry("500x400")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()

    tk.Label(ventana, text="Panel de Instructor",
             font=("Helvetica", 16, "bold")).pack(pady=20)

    tk.Label(ventana, text="Gestión de Clases",
             font=("Helvetica", 12)).pack(pady=10)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=20)

    tk.Button(frame_botones, text="Agregar una Clase",
              command=agregar_clase,
              bg="#4CAF50", fg="white",
              font=("Helvetica", 11, "bold"),
              width=18, height=2).pack(pady=10)

    tk.Button(frame_botones, text="Quitar una Clase",
              command=quitar_clase,
              bg="#f44336", fg="white",
              font=("Helvetica", 11, "bold"),
              width=18, height=2).pack(pady=10)

    tk.Button(frame_botones, text="Ver Todas las Clases",
              command=ver_clases_instructor,
              bg="#2196F3", fg="white",
              font=("Helvetica", 11, "bold"),
              width=18, height=2).pack(pady=10)

    tk.Button(ventana, text="Cerrar Sesión", command=ventana.destroy,
              bg="#9E9E9E", fg="white", font=("Helvetica", 10),
              width=15).pack(pady=20)


def agregar_clase():
    ventana = tk.Toplevel(window)
    ventana.title("Agregar Clase")
    ventana.geometry("450x400")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Nueva Clase de Pilates",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    tk.Label(ventana, text="Nombre de la clase:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana, width=35)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana, text="Día (ej: Lunes, Martes):").pack(pady=5)
    entrada_dia = tk.Entry(ventana, width=35)
    entrada_dia.pack(pady=5)

    tk.Label(ventana, text="Hora (ej: 08:00, 14:30):").pack(pady=5)
    entrada_hora = tk.Entry(ventana, width=35)
    entrada_hora.pack(pady=5)

    tk.Label(ventana, text="Cupo máximo:").pack(pady=5)
    entrada_cupo = tk.Entry(ventana, width=35)
    entrada_cupo.pack(pady=5)

    def guardar_clase():
        nombre = entrada_nombre.get().strip()
        dia = entrada_dia.get().strip()
        hora = entrada_hora.get().strip()
        cupo = entrada_cupo.get().strip()

        if not nombre or not dia or not hora or not cupo:
            messagebox.showwarning("Completa todos los campos")
            return

        try:
            cupo = int(cupo)
            if cupo <= 0:
                raise ValueError
        except:
            messagebox.showerror("El cupo debe ser un número positivo")
            return

        clase_id = len(CLASES) + 1
        nueva_clase = {
            'id': clase_id,
            'nombre': nombre,
            'dia': dia,
            'hora': hora,
            'cupo_maximo': cupo,
            'inscritos': 0,
            'alumnos': []
        }

        CLASES.append(nueva_clase)
        messagebox.showinfo("Éxito", f"¡Clase '{nombre}' agregada exitosamente!")
        ventana.destroy()

    tk.Button(ventana, text="Agregar Clase", command=guardar_clase,
              bg="#4CAF50", fg="white", font=("Helvetica", 11, "bold"),
              width=15, height=2).pack(pady=15)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#f44336", fg="white", font=("Helvetica", 10),
              width=15).pack()