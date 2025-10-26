import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import database
from database import verificar_usuario_existente, Usuario

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


# btn_frame = tk.Frame(ventana)
# btn_frame.pack(pady=20)
#
# tk.Button(btn_frame, text="Instructor", command=login_instructor,
#           bg="#2196F3", fg="white", font=("Helvetica", 11, "bold"),
#           width=12, height=2).pack(side=tk.LEFT, padx=10)
#
# tk.Button(btn_frame, text="Cliente", command=login_cliente,
#           bg="#FF9800", fg="white", font=("Helvetica", 11, "bold"),
#           width=12, height=2).pack(side=tk.LEFT, padx=10)


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


def quitar_clase():
    if not CLASES:
        messagebox.showinfo("No hay clases registradas")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Quitar Clase")
    ventana.geometry("500x400")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Selecciona la clase a eliminar",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    frame_lista = tk.Frame(ventana)
    frame_lista.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 10), height=10)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in CLASES:
        texto = f"ID:{clase['id']} - {clase['nombre']} | {clase['dia']} {clase['hora']} | Inscritos: {clase['inscritos']}/{clase['cupo_maximo']}"
        lista.insert(tk.END, texto)

    def eliminar_seleccionada():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Selecciona una clase")
            return

        indice = seleccion[0]
        clase = CLASES[indice]

        respuesta = messagebox.askyesno("Confirmar",
                                        f"¿Eliminar la clase '{clase['nombre']}'?\n"
                                        f"Hay {clase['inscritos']} alumno(s) inscrito(s).")
        if respuesta:
            # Remover inscripciones de clientes
            for cliente_nombre in list(INSCRIPCIONES.keys()):
                if clase['id'] in INSCRIPCIONES[cliente_nombre]:
                    INSCRIPCIONES[cliente_nombre].remove(clase['id'])

            CLASES.pop(indice)
            messagebox.showinfo("Clase eliminada exitosamente")
            ventana.destroy()

    tk.Button(ventana, text="Eliminar Clase", command=eliminar_seleccionada,
              bg="#f44336", fg="white", font=("Helvetica", 11, "bold"),
              width=15, height=2).pack(pady=10)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#9E9E9E", fg="white", font=("Helvetica", 10),
              width=15).pack()


def ver_clases_instructor():
    if not CLASES:
        messagebox.showinfo("Información", "No hay clases registradas")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Todas las Clases")
    ventana.geometry("600x450")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Lista de Clases Registradas",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tabla)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(frame_tabla, yscrollcommand=scrollbar.set,
                    font=("Courier", 10), height=15, width=70)
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)

    for clase in CLASES:
        info = f"{'=' * 60}\n"
        info += f"ID: {clase['id']}\n"
        info += f"Nombre: {clase['nombre']}\n"
        info += f"Día: {clase['dia']} | Hora: {clase['hora']}\n"
        info += f"Inscritos: {clase['inscritos']}/{clase['cupo_maximo']}\n"
        if clase['alumnos']:
            info += f"Alumnos: {', '.join(clase['alumnos'])}\n"
        info += f"{'=' * 60}\n\n"
        texto.insert(tk.END, info)

    texto.config(state=tk.DISABLED)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy,
              bg="#2196F3", fg="white", font=("Helvetica", 10),
              width=15).pack(pady=10)


# Panel del Cliente
def panel_cliente(nombre_cliente):
    ventana = tk.Toplevel(window)
    ventana.title("Panel de Cliente")
    ventana.geometry("500x450")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()

    tk.Label(ventana, text=f"Bienvenido, {nombre_cliente}",
             font=("Helvetica", 16, "bold")).pack(pady=20)

    tk.Label(ventana, text="¿Qué deseas hacer?",
             font=("Helvetica", 12)).pack(pady=10)

    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=20)

    tk.Button(frame_botones, text="Ver Horarios Disponibles",
              command=lambda: ver_horarios_disponibles(nombre_cliente),
              bg="#2196F3", fg="white",
              font=("Helvetica", 11, "bold"),
              width=22, height=2).pack(pady=10)

    tk.Button(frame_botones, text="Asignarse a una Clase",
              command=lambda: asignarse_clase(nombre_cliente),
              bg="#4CAF50", fg="white",
              font=("Helvetica", 11, "bold"),
              width=22, height=2).pack(pady=10)

    tk.Button(frame_botones, text="Salirse de una Clase",
              command=lambda: salirse_clase(nombre_cliente),
              bg="#FF9800", fg="white",
              font=("Helvetica", 11, "bold"),
              width=22, height=2).pack(pady=10)

    tk.Button(frame_botones, text="Mis Clases Inscritas",
              command=lambda: ver_mis_clases(nombre_cliente),
              bg="#9C27B0", fg="white",
              font=("Helvetica", 11, "bold"),
              width=22, height=2).pack(pady=10)

    tk.Button(ventana, text="Cerrar Sesión", command=ventana.destroy,
              bg="#9E9E9E", fg="white", font=("Helvetica", 10),
              width=15).pack(pady=15)


def ver_horarios_disponibles(nombre_cliente):
    if not CLASES:
        messagebox.showinfo("Información", "No hay clases disponibles aún")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Horarios Disponibles")
    ventana.geometry("600x450")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Horarios de Clases Disponibles",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tabla)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(frame_tabla, yscrollcommand=scrollbar.set,
                    font=("Courier", 10), height=15, width=70)
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)

    # Inicializar inscripciones del cliente si no existen
    if nombre_cliente not in INSCRIPCIONES:
        INSCRIPCIONES[nombre_cliente] = []

    for clase in CLASES:
        disponibilidad = "LLENO" if clase['inscritos'] >= clase['cupo_maximo'] else "DISPONIBLE"
        inscrito = "✓ YA INSCRITO" if clase['id'] in INSCRIPCIONES[nombre_cliente] else ""

        info = f"{'=' * 60}\n"
        info += f"Clase: {clase['nombre']}\n"
        info += f"Día: {clase['dia']} | Hora: {clase['hora']}\n"
        info += f"Cupos: {clase['inscritos']}/{clase['cupo_maximo']} | Estado: {disponibilidad}\n"
        if inscrito:
            info += f"{inscrito}\n"
        info += f"{'=' * 60}\n\n"
        texto.insert(tk.END, info)

    texto.config(state=tk.DISABLED)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy,
              bg="#2196F3", fg="white", font=("Helvetica", 10),
              width=15).pack(pady=10)


def asignarse_clase(nombre_cliente):
    if not CLASES:
        messagebox.showinfo("Información", "No hay clases disponibles")
        return

    # Inicializar inscripciones del cliente
    if nombre_cliente not in INSCRIPCIONES:
        INSCRIPCIONES[nombre_cliente] = []

    # Filtrar clases disponibles
    clases_disponibles = [c for c in CLASES if c['inscritos'] < c['cupo_maximo']
                          and c['id'] not in INSCRIPCIONES[nombre_cliente]]

    if not clases_disponibles:
        messagebox.showinfo("Información", "No hay clases disponibles o ya estás inscrito en todas")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Asignarse a Clase")
    ventana.geometry("550x400")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Selecciona una clase para inscribirte",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    frame_lista = tk.Frame(ventana)
    frame_lista.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 10), height=10)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in clases_disponibles:
        texto = f"{clase['nombre']} | {clase['dia']} {clase['hora']} | Cupos: {clase['inscritos']}/{clase['cupo_maximo']}"
        lista.insert(tk.END, texto)

    def inscribirse():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return

        indice = seleccion[0]
        clase = clases_disponibles[indice]

        # Encontrar la clase en CLASES y actualizar
        for c in CLASES:
            if c['id'] == clase['id']:
                c['inscritos'] += 1
                c['alumnos'].append(nombre_cliente)
                break

        INSCRIPCIONES[nombre_cliente].append(clase['id'])

        messagebox.showinfo("Éxito", f"¡Te has inscrito a '{clase['nombre']}'!")
        ventana.destroy()

    tk.Button(ventana, text="Inscribirme", command=inscribirse,
              bg="#4CAF50", fg="white", font=("Helvetica", 11, "bold"),
              width=15, height=2).pack(pady=10)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#9E9E9E", fg="white", font=("Helvetica", 10),
              width=15).pack()


def salirse_clase(nombre_cliente):
    if nombre_cliente not in INSCRIPCIONES or not INSCRIPCIONES[nombre_cliente]:
        messagebox.showinfo("Información", "No estás inscrito en ninguna clase")
        return

    # Obtener clases en las que está inscrito
    mis_clases = [c for c in CLASES if c['id'] in INSCRIPCIONES[nombre_cliente]]

    ventana = tk.Toplevel(window)
    ventana.title("Salirse de Clase")
    ventana.geometry("550x400")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Selecciona la clase de la que deseas salir",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    frame_lista = tk.Frame(ventana)
    frame_lista.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 10), height=10)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in mis_clases:
        texto = f"{clase['nombre']} | {clase['dia']} {clase['hora']}"
        lista.insert(tk.END, texto)

    def desinscribirse():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return

        indice = seleccion[0]
        clase = mis_clases[indice]

        respuesta = messagebox.askyesno("Confirmar",
                                        f"¿Deseas salir de '{clase['nombre']}'?")
        if respuesta:
            # Actualizar clase
            for c in CLASES:
                if c['id'] == clase['id']:
                    c['inscritos'] -= 1
                    c['alumnos'].remove(nombre_cliente)
                    break

            INSCRIPCIONES[nombre_cliente].remove(clase['id'])

            messagebox.showinfo("Éxito", f"Te has dado de baja de '{clase['nombre']}'")
            ventana.destroy()

    tk.Button(ventana, text="Salir de Clase", command=desinscribirse,
              bg="#FF9800", fg="white", font=("Helvetica", 11, "bold"),
              width=15, height=2).pack(pady=10)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#9E9E9E", fg="white", font=("Helvetica", 10),
              width=15).pack()


def ver_mis_clases(nombre_cliente):
    if nombre_cliente not in INSCRIPCIONES or not INSCRIPCIONES[nombre_cliente]:
        messagebox.showinfo("Información", "No estás inscrito en ninguna clase")
        return

    mis_clases = [c for c in CLASES if c['id'] in INSCRIPCIONES[nombre_cliente]]

    ventana = tk.Toplevel(window)
    ventana.title("Mis Clases")
    ventana.geometry("550x400")
    ventana.resizable(False, False)
    ventana.grab_set()

    tk.Label(ventana, text="Mis Clases Inscritas",
             font=("Helvetica", 14, "bold")).pack(pady=15)

    frame_tabla = tk.Frame(ventana)
    frame_tabla.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tabla)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(frame_tabla, yscrollcommand=scrollbar.set,
                    font=("Courier", 10), height=12, width=60)
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)

    for clase in mis_clases:
        info = f"{'=' * 50}\n"
        info += f"Clase: {clase['nombre']}\n"
        info += f"Día: {clase['dia']}\n"
        info += f"Hora: {clase['hora']}\n"
        info += f"{'=' * 50}\n\n"
        texto.insert(tk.END, info)

    texto.config(state=tk.DISABLED)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy,
              bg="#9C27B0", fg="white", font=("Helvetica", 10),
              width=15).pack(pady=10)

#Ventana de registro
def ventana_registrarse():
    ventana = tk.Toplevel(window)
    ventana.title("Registrarse")
    ventana.geometry("400x300")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()

    tk.Label(ventana, text="Registro de Cliente",
             font=("Helvetica", 14, "bold")).pack(pady=20)

    tk.Label(ventana, text="Nombre completo:").pack(pady=5)
    entrada_nombre = tk.Entry(ventana, width=35)
    entrada_nombre.pack(pady=5)

    tk.Label(ventana, text="Número de celular:").pack(pady=5)
    entrada_celular = tk.Entry(ventana, width=35)
    entrada_celular.pack(pady=5)

    def guardar_cliente():
        nombre = entrada_nombre.get().strip()
        celular = entrada_celular.get().strip()

        if not nombre or not celular:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return

        if verificar_usuario_existente(nombre,celular):
            messagebox.showwarning("Advertencia", "El usuario ya está registrado")
            return
        nuevo_usuario = Usuario(nombre,celular,"cliente")
        nuevo_usuario.guardar()
        messagebox.showinfo("Éxito", f"¡Cliente {nombre} registrado exitosamente!\nAhora puedes iniciar sesión.")
        ventana.destroy()

    btn_registrar= tk.Button(ventana, text="Registrar", command=guardar_cliente,
                            bg="#4CAF50", fg="white", font=("Helvetica", 11, "bold"),
                            width=15, height=2)
    btn_registrar.pack(pady=20)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#f44336", fg="white", font=("Helvetica", 10),
              width=15).pack()


# Ventana principal
window = tk.Tk()
window.title("DAC PILATES")
window.geometry("750x400")
window.resizable(False, False)

frame_principal = tk.Frame(window)
frame_principal.pack(fill=tk.BOTH, expand=True)

frame_izquierdo = tk.Frame(frame_principal, width=400)
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20)

tk.Label(frame_izquierdo, text="Bienvenido a la gestión de DAC",
         font=("Helvetica", 18, "bold")).pack(pady=40)

tk.Label(frame_izquierdo, text="Selecciona una opción:",
         font=("Helvetica", 12)).pack(pady=20)

frame_botones = tk.Frame(frame_izquierdo)
frame_botones.pack(pady=30)

btn_login = tk.Button(frame_botones, text="Iniciar Sesión",
                      command=ventana_iniciar_sesion,
                      bg="#2196F3", fg="white",
                      font=("Helvetica", 12, "bold"),
                      width=15, height=2)
btn_login.pack(pady=10)

btn_registro = tk.Button(frame_botones, text="Registrarse",
                         command=ventana_registrarse,
                         bg="#4CAF50", fg="white",
                         font=("Helvetica", 12, "bold"),
                         width=15, height=2)
btn_registro.pack(pady=10)

frame_derecho = tk.Frame(frame_principal, width=350, bg="#f0f0f0")
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

try:
    from PIL import Image, ImageTk

    imagen = Image.open('Dac logo png.png')
    imagen = imagen.resize((330, 380), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame_derecho, image=photo, bg="#f0f0f0")
    label_imagen.image = photo
    label_imagen.pack(pady=10)
except Exception as e:
    tk.Label(frame_derecho, text="\n\nDAC\n\nPILATES",
             font=("Helvetica", 36, "bold"),
             bg="#f0f0f0",
             fg="#2196F3").pack(expand=True)

window.mainloop()