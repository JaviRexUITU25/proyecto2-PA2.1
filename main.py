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
