import tkinter as tk
from tkinter import messagebox, ttk
import database
database.crear_tablas()
#VENTANA PARA INICIAR SESION
def ventana_iniciar_sesion():
    ventana = tk.Toplevel(window)
    ventana.title("Iniciar Sesión")
    ventana.geometry("550x420")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="🔐 Iniciar Sesión",
             font=("Helvetica", 14, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=40)

    tk.Label(ventana, text="Código de Usuario:",
             bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=5)
    entrada_codigo = tk.Entry(ventana, width=40, font=("Helvetica", 11))
    entrada_codigo.pack(pady=8)

    tk.Label(ventana, text="Número de Teléfono:",
             bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=5)
    entrada_telefono = tk.Entry(ventana, width=40, font=("Helvetica", 11))
    entrada_telefono.pack(pady=8)

    def validar_login():
        codigo = entrada_codigo.get().strip()
        telefono = entrada_telefono.get().strip()

        if not codigo or not telefono:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return
        usuario = database.Usuario.verificar_inicio_sesion(codigo, telefono)

        if not usuario:
            messagebox.showerror("Error", "Código o teléfono incorrectos.")
            return

        nombre = usuario["nombre"]
        tipo = usuario["tipo"]
        messagebox.showinfo("Bienvenido", f"¡Hola {nombre}! Iniciaste sesión como {tipo}.")
        ventana.destroy()
        if tipo.lower() == "instructor":
            panel_instructor()
        else:
            panel_cliente(nombre, telefono)

    tk.Button(ventana, text="Ingresar", command=validar_login,
              bg="#6B9080", fg="white", font=("Helvetica", 12, "bold"),
              width=18, height=2, cursor="hand2").pack(pady=25)

    def ventana_recuperar_codigo():
        ventana = tk.Toplevel(window)
        ventana.title("Recuperar Código de Usuario")
        ventana.geometry("550x350")
        ventana.resizable(False, False)
        ventana.transient(window)
        ventana.grab_set()
        ventana.configure(bg="#F5F0E8")

        tk.Label(ventana, text="Recuperar tu código de usuario",
                 font=("Helvetica", 14, "bold"),  bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

        tk.Label(ventana, text="Nombre completo:",  bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=5)
        entrada_nombre = tk.Entry(ventana, width=35, font=("Helvetica", 11))
        entrada_nombre.pack(pady=8)

        tk.Label(ventana, text="Número de teléfono:",  bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=5)
        entrada_telefono = tk.Entry(ventana, width=35, font=("Helvetica", 11))
        entrada_telefono.pack(pady=8)

        def buscar_codigo():
            nombre = entrada_nombre.get().strip()
            telefono = entrada_telefono.get().strip()

            if not nombre or not telefono:
                messagebox.showwarning("Advertencia", "Completa todos los campos")
                return

            codigo = database.Usuario.recuperar_codigo(nombre, telefono)

            if codigo:
                messagebox.showinfo("Tu código de usuario",
                                    f"{nombre} tu código de usuario es: {codigo}")
                ventana.destroy()
            else:
                messagebox.showerror("Error", "No se encontró un usuario con esos datos.")

        tk.Button(ventana, text="Buscar Código", command=buscar_codigo,
                  bg="#6B9080", fg="white", font=("Helvetica", 11, "bold"),
                  width=18, height=2, cursor="hand2").pack(pady=20)

        tk.Button(ventana, text="Cancelar", command=ventana.destroy,
                  bg="#9E9E9E", fg="white", font=("Helvetica", 10, "bold"),
                  width=18, height=2, cursor="hand2").pack(pady=5)

    tk.Button(ventana, text="¿Olvidaste tu código?",
              command=ventana_recuperar_codigo,
              bg="#9E9E9E", fg="white", font=("Helvetica", 10, "bold"),
              width=18, height=2, cursor="hand2").pack()

#PUNTO DE VISTA PARA EL INSTRUCTOR
def panel_instructor():
    ventana = tk.Toplevel(window)
    ventana.title("Panel de Instructor")
    ventana.geometry("750x700")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="📋 Panel de Instructor",
             font=("Helvetica", 18, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=30)

    tk.Label(ventana, text="Gestión de Clases",
             font=("Helvetica", 13), bg="#F5F0E8", fg="#6B9080").pack(pady=15)

    frame_botones = tk.Frame(ventana, bg="#F5F0E8")
    frame_botones.pack(pady=25)

    tk.Button(frame_botones, text="➕ Agregar una Clase",
              command=agregar_clase,
              bg="#6B9080", fg="white",
              font=("Helvetica", 12, "bold"),
              width=22, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="➖ Quitar una Clase",
              command=quitar_clase,
              bg="#EAA4A4", fg="white",
              font=("Helvetica", 12, "bold"),
              width=22, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="📚 Ver Todas las Clases",
              command=ver_clases_instructor,
              bg="#A4C3B2", fg="white",
              font=("Helvetica", 12, "bold"),
              width=22, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="✏️ Actualizar Clase",
              command=actualizar_clase,
              bg="#F7D6E0", fg="#2C3E50",
              font=("Helvetica", 12, "bold"),
              width=22, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="📋 Registrar Asistencia",
              command=registrar_asistencia,
              bg="#6B9080", fg="white",
              font=("Helvetica", 12, "bold"),
              width=22,height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="🚪 Cerrar Sesión", command=ventana.destroy,
              bg="#B0B0B0", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack(pady=25)


#FUNCION PARA AGREGAR UNA CLASE
def agregar_clase():
    ventana = tk.Toplevel(window)
    ventana.title("Agregar Clase")
    ventana.geometry("600x550")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="✨ Nueva Clase de Pilates",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    tk.Label(ventana, text="Nombre de la clase:", bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=8)
    entrada_nombre = tk.Entry(ventana, width=40, font=("Helvetica", 11))
    entrada_nombre.pack(pady=8)

    tk.Label(ventana, text="Selecciona un horario:",
             bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=8)

    horarios = database.Horario.listar()
    opciones = [f"{h['dia']} {h['hora_inicio']} - {h['hora_fin']}" for h in horarios]

    seleccion_horario = ttk.Combobox(ventana, values=opciones, state="readonly",
                                     font=("Helvetica", 11), width=45)
    seleccion_horario.pack(pady=8)

    tk.Label(ventana, text="Cupo máximo:", bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=8)
    entrada_cupo = tk.Entry(ventana, width=40, font=("Helvetica", 11))
    entrada_cupo.pack(pady=8)

#FUNCION PARA GUARDAR UNA CLASE
    def guardar_clase():
        nombre = entrada_nombre.get().strip()
        horario = seleccion_horario.current()
        cupo = entrada_cupo.get().strip()

        if not nombre or horario == -1 or not cupo:
            messagebox.showwarning("Error"," ❌ Completa todos los campos")
            return

        try:
            cupo = int(cupo)
            if cupo <= 0:
                messagebox.showwarning("Error", " ❌ El cupo debe ser positivo")
                return
        except ValueError:
            messagebox.showwarning("Error", "❌ El cupo debe ser un número entero positivo")
            return

        id_horario = horarios[horario]['id_horario']

        nueva_clase = database.Sesion(nombre,id_horario, cupo)
        nueva_clase.guardar()
        messagebox.showinfo("Éxito", f"¡Clase '{nombre}' agregada exitosamente!")
        ventana.destroy()

    tk.Button(ventana, text="✅ Agregar Clase", command=guardar_clase,
              bg="#6B9080", fg="white", font=("Helvetica", 12, "bold"),
              width=18, height=2, cursor="hand2").pack(pady=20)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#EAA4A4", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()

#FUNCION PARA QUITAR UNA CLASE
def quitar_clase():
    clases = database.Sesion.listar()
    if not clases:
        messagebox.showinfo("No hay clases registradas")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Quitar Clase")
    ventana.geometry("650x600")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="🗑️ Selecciona la clase a eliminar",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    frame_lista = tk.Frame(ventana, bg="#F5F0E8")
    frame_lista.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 11), height=12)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in clases:
        texto = f"ID:{clase['id_sesion']} - {clase['nombre']} | {clase['dia']} Hora:{clase['hora_inicio']} - {clase['hora_fin']} | Cupo: {clase['cupo']}"
        lista.insert(tk.END, texto)
#QUITAR LA CLASE SELECCIONADA
    def eliminar_seleccionada():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una clase")
            return

        indice = seleccion[0]
        clase = clases[indice]

        respuesta = messagebox.askyesno("Confirmar",
                                        f"¿Eliminar la clase '{clase['nombre']}' del día {clase['dia']}?")

        if respuesta:
            database.Sesion.eliminar(clase['id_sesion'])
            messagebox.showinfo("¡Exito!", "Clase eliminada exitosamente")
            ventana.destroy()

    tk.Button(ventana, text="🗑️ Eliminar Clase", command=eliminar_seleccionada,
              bg="#EAA4A4", fg="white", font=("Helvetica", 12, "bold"),
              width=18, height=2, cursor="hand2").pack(pady=15)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#B0B0B0", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()

#FUNCION PARA QUE EL INSTRUCTOR VEA LAS CLASES REGISTRADAS
def ver_clases_instructor():
    clases = database.Sesion.listar()
    if not clases:
        messagebox.showinfo("Información", "No hay clases registradas")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Todas las Clases")
    ventana.geometry("750x600")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="📚 Lista de Clases Registradas",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    frame_tabla = tk.Frame(ventana, bg="#F5F0E8")
    frame_tabla.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tabla)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_tabla, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 11), height=18, width=80)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in clases:
        texto = f"Nombre:{clase['nombre']} | {clase['dia']} {clase['hora_inicio']} - {clase['hora_fin']} | Cupo: {clase['cupo']}"
        lista.insert(tk.END, texto)

    def mostrar_inscritos():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return
        clase = clases[seleccion[0]]
        id_sesion = clase['id_sesion']

        # Traer inscritos y asistencias
        inscritos = database.Inscripcion.listar_por_sesion(id_sesion)
        if not inscritos:
            messagebox.showinfo("Información",
                                f"No hay clientes inscritos en la clase '{clase['nombre']}'.")
            return
        asistencias = database.Asistencia.listar_por_sesion(id_sesion)

        presentes = set(a['id_usuario'] for a in asistencias if a['presente'])

        ventana_inscritos = tk.Toplevel(ventana)
        ventana_inscritos.title("Inscritos y Asistencia")
        ventana_inscritos.geometry("600x500")
        ventana_inscritos.grab_set()
        ventana_inscritos.configure(bg="#F5F0E8")

        tk.Label(ventana_inscritos, text=f"Inscritos en '{clase['nombre']}'",
                 font=("Helvetica", 15, "bold"), bg="#F5F0E8").pack(pady=15)

        frame = tk.Frame(ventana_inscritos, bg="#F5F0E8")
        frame.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        texto = tk.Text(frame, font=("Courier", 11), height=20, width=60, bg="#FFFFFF")
        texto.pack(fill=tk.BOTH, expand=True)

        for usuario in inscritos:
            estado = "✅ Presente" if usuario['id_usuario'] in presentes else "❌ Ausente"
            texto.insert(tk.END, f"{usuario['nombre']} ({usuario['telefono']}) - {estado}\n")

        texto.config(state=tk.DISABLED)

        tk.Button(ventana_inscritos, text="Cerrar", command=ventana_inscritos.destroy,
                  bg="#A4C3B2", fg="white", font=("Helvetica", 11),
                  width=18, cursor="hand2").pack(pady=15)

    tk.Button(ventana, text="👥 Ver Inscritos y Asistencia", command=mostrar_inscritos,
              bg="#CCE3DE", fg="#2C3E50", font=("Helvetica", 12, "bold"),
              width=28, height=2, cursor="hand2").pack(pady=10)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy,
              bg="#A4C3B2", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack(pady=15)

def actualizar_clase():
    clases = database.Sesion.listar()
    if not clases:
        messagebox.showinfo("Información", "No hay clases para actualizar")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Actualizar Clase")
    ventana.geometry("700x600")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="Selecciona la clase a actualizar",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    lista = tk.Listbox(ventana, font=("Helvetica", 11), height=10, width=80)
    lista.pack(pady=10)

    for clase in clases:
        texto = f"ID:{clase['id_sesion']} - {clase['nombre']} | {clase['dia']} {clase['hora_inicio']} - {clase['hora_fin']} | Cupo: {clase['cupo']}"
        lista.insert(tk.END, texto)

    def editar():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return
        clase = clases[seleccion[0]]

        ventana_editar = tk.Toplevel(ventana)
        ventana_editar.title("Editar Clase")
        ventana_editar.geometry("500x400")
        ventana_editar.grab_set()
        ventana_editar.configure(bg="#F5F0E8")

        tk.Label(ventana_editar, text="Editar Clase", font=("Helvetica", 14, "bold"), bg="#F5F0E8").pack(pady=15)
        tk.Label(ventana_editar, text="Nombre:", bg="#F5F0E8").pack()
        entrada_nombre = tk.Entry(ventana_editar, width=40)
        entrada_nombre.insert(0, clase['nombre'])
        entrada_nombre.pack(pady=5)

        tk.Label(ventana_editar, text="Cupo:", bg="#F5F0E8").pack()
        entrada_cupo = tk.Entry(ventana_editar, width=40)
        entrada_cupo.insert(0, clase['cupo'])
        entrada_cupo.pack(pady=5)

        tk.Label(ventana_editar, text="Horario:", bg="#F5F0E8").pack()
        horarios = database.Horario.listar()
        opciones = [f"{h['dia']} {h['hora_inicio']} - {h['hora_fin']}" for h in horarios]
        seleccion_horario = ttk.Combobox(ventana_editar, values=opciones, state="readonly", width=37)
        for idx, h in enumerate(horarios):
            if h['dia'] == clase['dia'] and h['hora_inicio'] == clase['hora_inicio'] and h['hora_fin'] == clase['hora_fin']:
                seleccion_horario.current(idx)
                break
        seleccion_horario.pack(pady=5)

        def guardar_cambios():
            nuevo_nombre = entrada_nombre.get().strip()
            nuevo_cupo = entrada_cupo.get().strip()
            idx_horario = seleccion_horario.current()
            if not nuevo_nombre or not nuevo_cupo or idx_horario == -1:
                messagebox.showwarning("Advertencia", "Completa todos los campos")
                return
            try:
                nuevo_cupo = int(nuevo_cupo)
                if nuevo_cupo <= 0:
                    messagebox.showerror("Error", " ❌ El cupo debe ser un número positivo")
                    return
            except ValueError:
                messagebox.showerror("Error", "❌ El cupo debe ser un número entero positivo")
                return

            id_horario = horarios[idx_horario]['id_horario']
            database.Sesion.actualizar(clase['id_sesion'], nuevo_nombre, id_horario, nuevo_cupo)
            messagebox.showinfo("Éxito", "Clase actualizada correctamente")
            ventana_editar.destroy()
            ventana.destroy()

        tk.Button(ventana_editar, text="Guardar Cambios", command=guardar_cambios,
                  bg="#6B9080", fg="white", font=("Helvetica", 11, "bold"),
                  width=18, height=2, cursor="hand2").pack(pady=20)

        tk.Button(ventana_editar, text="Cancelar", command=ventana.destroy,
                  bg="#B0B0B0", fg="white", font=("Helvetica", 11),
                  width=18, cursor="hand2").pack()

    tk.Button(ventana, text="Editar Clase Seleccionada", command=editar,
              bg="#F7D6E0", fg="#2C3E50", font=("Helvetica", 12, "bold"),
              width=22, height=2, cursor="hand2").pack(pady=15)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#B0B0B0", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()

from datetime import date

def registrar_asistencia():
    sesiones = database.Sesion.listar()
    if not sesiones:
        messagebox.showinfo("Información", "No hay clases registradas")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Registrar Asistencia")
    ventana.geometry("650x600")
    ventana.configure(bg="#F5F0E8")
    ventana.grab_set()

    tk.Label(ventana, text="Selecciona la clase:", bg="#F5F0E8").pack(pady=10)
    nombres_clases = [f"{s['nombre']} | {s['dia']} {s['hora_inicio']}-{s['hora_fin']} " for s in sesiones]
    combo_clase = ttk.Combobox(ventana, values=nombres_clases, state="readonly", width=40)
    combo_clase.pack(pady=5)

    lista_usuarios = tk.Listbox(ventana, selectmode=tk.MULTIPLE, width=50)
    lista_usuarios.pack(pady=15)

    def cargar_usuarios(event=None):
        lista_usuarios.delete(0, tk.END)
        idx_clase = combo_clase.current()
        if idx_clase == -1:
            return
        id_sesion = sesiones[idx_clase]['id_sesion']
        inscritos = database.Inscripcion.listar_por_sesion(id_sesion)
        for usuario in inscritos:
            lista_usuarios.insert(tk.END, f"{usuario['nombre']} ({usuario['telefono']})")

    combo_clase.bind("<<ComboboxSelected>>", cargar_usuarios)

    def guardar_asistencia():
        idx_clase = combo_clase.current()
        if idx_clase == -1:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return
        seleccionados = lista_usuarios.curselection()
        if not seleccionados:
            messagebox.showwarning("Advertencia", "Selecciona al menos un usuario")
            return
        id_sesion = sesiones[idx_clase]['id_sesion']
        inscritos = database.Inscripcion.listar_por_sesion(id_sesion)
        fecha = date.today().isoformat()
        for idx in seleccionados:
            id_usuario = inscritos[idx]['id_usuario']
            asistencia = database.Asistencia(id_usuario, id_sesion, fecha, 1)
            asistencia.guardar()
        messagebox.showinfo("Éxito", "¡Asistencia registrada!")
        ventana.destroy()

    tk.Button(ventana, text="Registrar Asistencia", command=guardar_asistencia,
              bg="#6B9080", fg="white", font=("Helvetica", 12, "bold"),
              width=20, height=2, cursor="hand2").pack(pady=10)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#EAA4A4", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()


#VENTANA COMO CLIENTE
def panel_cliente(nombre_cliente, telefono_cliente=""):
    ventana = tk.Toplevel(window)
    ventana.title("Panel de Cliente")
    ventana.geometry("650x600")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text=f"👋 Bienvenido, {nombre_cliente}",
             font=("Helvetica", 18, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=30)

    tk.Label(ventana, text="¿Qué deseas hacer?",
             font=("Helvetica", 13), bg="#F5F0E8", fg="#6B9080").pack(pady=15)

    frame_botones = tk.Frame(ventana, bg="#F5F0E8")
    frame_botones.pack(pady=25)

    tk.Button(frame_botones, text="📅 Ver Horarios Disponibles",
              command=lambda: ver_horarios_disponibles(nombre_cliente),
              bg="#A4C3B2", fg="white",
              font=("Helvetica", 12, "bold"),
              width=26, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="✅ Asignarse a una Clase",
              command=lambda: asignarse_clase(nombre_cliente, telefono_cliente),
              bg="#6B9080", fg="white",
              font=("Helvetica", 12, "bold"),
              width=26, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="❌ Salirse de una Clase",
              command=lambda: salirse_clase(nombre_cliente, telefono_cliente),
              bg="#EAA4A4", fg="white",
              font=("Helvetica", 12, "bold"),
              width=26, height=2, cursor="hand2").pack(pady=12)

    tk.Button(frame_botones, text="📝 Mis Clases Inscritas",
              command=lambda: ver_mis_clases(nombre_cliente, telefono_cliente),
              bg="#CCE3DE", fg="#2C3E50",
              font=("Helvetica", 12, "bold"),
              width=26, height=2, cursor="hand2").pack(pady=12)

    tk.Button(ventana, text="🚪 Cerrar Sesión", command=ventana.destroy,
              bg="#B0B0B0", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack(pady=20)

#FUNCION PARA VER LOS HORARIOS DISPONIBLES
def ver_horarios_disponibles(nombre_cliente):
    clases = database.Sesion.listar()
    if not clases:
        messagebox.showinfo("Información", "No hay clases disponibles aún")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Horarios Disponibles")
    ventana.geometry("750x550")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="📅 Horarios de Clases Disponibles",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    frame_tabla = tk.Frame(ventana, bg="#F5F0E8")
    frame_tabla.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tabla)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(frame_tabla, yscrollcommand=scrollbar.set,
                    font=("Courier", 11), height=18, width=80, bg="#FFFFFF")
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)

    for clase in clases:
        info = f"{'=' * 60}\n"
        info += f"Clase: {clase['nombre']}\n"
        info += f"Día: {clase['dia']} | Hora: {clase['hora_inicio']} - {clase['hora_fin']}\n"
        info += f"Cupo: {clase['cupo']}\n"
        info += f"{'=' * 60}\n\n"
        texto.insert(tk.END, info)

    texto.config(state=tk.DISABLED)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy,
              bg="#A4C3B2", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack(pady=15)

#FUNCION PARA SALIR DE LA CLASE
def asignarse_clase(nombre_cliente, telefono_cliente):
    id_usuario = database.Inscripcion.obtener_id_usuario(nombre_cliente, telefono_cliente)
    if not id_usuario:
        messagebox.showerror("Error", "Usuario no encontrado")
        return
    clases = database.Sesion.listar()
    if not clases:
        messagebox.showinfo("Información", "No hay clases disponibles")
        return

    clases_inscritas = database.Inscripcion.listar_por_usuario(id_usuario)
    id_sesiones_inscritas = [c["id_sesion"] for c in clases_inscritas]

    clases_disponibles = [c for c in clases if c["id_sesion"] not in id_sesiones_inscritas and c["cupo"] > 0]

    if not clases_disponibles:
        messagebox.showinfo("Información", "Ya estás inscrito en todas las clases disponibles")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Asignarse a Clase")
    ventana.geometry("700x500")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="✅ Selecciona una clase para inscribirte",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    frame_lista = tk.Frame(ventana, bg="#F5F0E8")
    frame_lista.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 11), height=12)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in clases_disponibles:
        texto = f"{clase['nombre']} | {clase['dia']} {clase['hora_inicio']} - {clase['hora_fin']} | Cupos: {clase['cupo']}"
        lista.insert(tk.END, texto)
# METERSE A UNA CLASE
    def inscribirse():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return

        clase = clases_disponibles[seleccion[0]]
        inscripcion = database.Inscripcion(id_usuario, clase["id_sesion"])
        resultado = inscripcion.guardar()
        if resultado == "inscrito":
            messagebox.showinfo("Éxito", f"¡Te has inscrito a '{clase['nombre']}'!")
        ventana.destroy()

    tk.Button(ventana, text="✅ Inscribirme", command=inscribirse,
              bg="#6B9080", fg="white", font=("Helvetica", 12, "bold"),
              width=18, height=2, cursor="hand2").pack(pady=15)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#B0B0B0", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()

#FUNCION PARA SALIR DE UNA CLASE
def salirse_clase(nombre_cliente, telefono_cliente):
    id_usuario = database.Inscripcion.obtener_id_usuario(nombre_cliente, telefono_cliente)
    if not id_usuario:
        messagebox.showerror("Error", "Usuario no encontrado")
        return
    clases = database.Inscripcion.listar_por_usuario(id_usuario)
    if not clases:
        messagebox.showinfo("Información", "No estás inscrito en ninguna clase")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Salirse de Clase")
    ventana.geometry("700x500")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="❌ Selecciona la clase de la que deseas salir",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    frame_lista = tk.Frame(ventana, bg="#F5F0E8")
    frame_lista.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_lista)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(frame_lista, yscrollcommand=scrollbar.set,
                       font=("Helvetica", 11), height=12)
    lista.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=lista.yview)

    for clase in clases:
        texto = f"{clase['nombre']} | {clase['dia']} {clase['hora_inicio']} - {clase['hora_fin']}"
        lista.insert(tk.END, texto)

    def desinscribirse():
        seleccion = lista.curselection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona una clase")
            return

        clase = clases[seleccion[0]]

        respuesta = messagebox.askyesno("Confirmar",
                                        f"¿Deseas salir de '{clase['nombre']}'?")
        if respuesta:
            database.Inscripcion.eliminar_inscripcion(id_usuario, clase["id_sesion"])
            messagebox.showinfo("Éxito", f"Te has dado de baja de '{clase['nombre']}'")
            ventana.destroy()

    tk.Button(ventana, text="❌ Salir de Clase", command=desinscribirse,
              bg="#EAA4A4", fg="white", font=("Helvetica", 12, "bold"),
              width=18, height=2, cursor="hand2").pack(pady=15)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#B0B0B0", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()

# FUNCION PARA VER MIS CLASES ASIGNADAS
def ver_mis_clases(nombre_cliente, telefono_cliente):
    id_usuario = database.Inscripcion.obtener_id_usuario(nombre_cliente, telefono_cliente)
    if not id_usuario:
        messagebox.showerror("Error", "Usuario no encontrado")
        return
    clases = database.Inscripcion.listar_por_usuario(id_usuario)
    if not clases:
        messagebox.showinfo("Información", "No estás inscrito en ninguna clase")
        return

    ventana = tk.Toplevel(window)
    ventana.title("Mis Clases")
    ventana.geometry("700x500")
    ventana.resizable(False, False)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="📝 Mis Clases Inscritas",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=20)

    frame_tabla = tk.Frame(ventana, bg="#F5F0E8")
    frame_tabla.pack(pady=15, padx=25, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame_tabla)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    texto = tk.Text(frame_tabla, yscrollcommand=scrollbar.set,
                    font=("Courier", 11), height=15, width=70, bg="#FFFFFF")
    texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=texto.yview)

    for clase in clases:
        info = f"{'=' * 50}\n"
        info += f"Clase: {clase['nombre']}\n"
        info += f"Día: {clase['dia']}\n"
        info += f"Hora: {clase['hora_inicio']} - {clase['hora_fin']}\n"
        info += f"{'=' * 50}\n\n"
        texto.insert(tk.END, info)

    texto.config(state=tk.DISABLED)

    tk.Button(ventana, text="Cerrar", command=ventana.destroy,
              bg="#CCE3DE", fg="#2C3E50", font=("Helvetica", 11),
              width=18, cursor="hand2").pack(pady=15)

# VENTANA DE REGISTRARSE
def ventana_registrarse():
    ventana = tk.Toplevel(window)
    ventana.title("Registrarse")
    ventana.geometry("550x400")
    ventana.resizable(False, False)
    ventana.transient(window)
    ventana.grab_set()
    ventana.configure(bg="#F5F0E8")

    tk.Label(ventana, text="📝 Registro de Cliente",
             font=("Helvetica", 16, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=25)

    tk.Label(ventana, text="Nombre completo:", bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=8)
    entrada_nombre = tk.Entry(ventana, width=40, font=("Helvetica", 11))
    entrada_nombre.pack(pady=8)

    tk.Label(ventana, text="Número de celular:", bg="#F5F0E8", fg="#2C3E50", font=("Helvetica", 11)).pack(pady=8)
    entrada_celular = tk.Entry(ventana, width=40, font=("Helvetica", 11))
    entrada_celular.pack(pady=8)
# GUARDAR USUARIO
    def guardar_cliente():
        nombre = entrada_nombre.get().strip()
        celular = entrada_celular.get().strip()

        if not nombre or not celular:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return

        if not (celular.isdigit() and len(celular) == 8):
            messagebox.showwarning("Advertencia", "El número de celular debe tener exactamente 8 dígitos")
            return

        if database.Usuario.verificar_usuario_existente(nombre, celular):
            messagebox.showwarning("Advertencia", "El usuario ya está registrado")
            return
        nuevo_usuario = database.Usuario(nombre, celular, "cliente")
        nuevo_usuario.guardar()
        codigo = nuevo_usuario.obtener_id()
        if codigo:
            messagebox.showinfo("Registro exitoso",
                                f"¡Cliente {nombre} registrado exitosamente!\n"
                                f"Tu código de usuario es: {codigo}\n"
                                f"Guárdalo, lo necesitarás para iniciar sesión.")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se pudo obtener el código del usuario.")

    btn_registrar = tk.Button(ventana, text="✅ Registrar", command=guardar_cliente,
                              bg="#6B9080", fg="white", font=("Helvetica", 12, "bold"),
                              width=18, height=2, cursor="hand2")
    btn_registrar.pack(pady=25)

    tk.Button(ventana, text="Cancelar", command=ventana.destroy,
              bg="#EAA4A4", fg="white", font=("Helvetica", 11),
              width=18, cursor="hand2").pack()


# Ventana principal
window = tk.Tk()
window.title("DAC PILATES 🧘‍♀️")
window.geometry("1920x1080")
window.state('zoomed')
window.configure(bg="#F5F0E8")

frame_principal = tk.Frame(window, bg="#F5F0E8")
frame_principal.pack(fill=tk.BOTH, expand=True)

frame_izquierdo = tk.Frame(frame_principal, bg="#F5F0E8")
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=80)

tk.Label(frame_izquierdo, text="🧘‍♀️ Bienvenido a DAC PILATES",
         font=("Helvetica", 28, "bold"), bg="#F5F0E8", fg="#2C3E50").pack(pady=80)

tk.Label(frame_izquierdo, text="BODY TRANSFORMATION",
         font=("Helvetica", 16), bg="#F5F0E8", fg="#6B9080").pack(pady=20)

tk.Label(frame_izquierdo, text="Selecciona una opción para comenzar",
         font=("Helvetica", 14), bg="#F5F0E8", fg="#2C3E50").pack(pady=40)

frame_botones = tk.Frame(frame_izquierdo, bg="#F5F0E8")
frame_botones.pack(pady=50)

btn_login = tk.Button(frame_botones, text="🔐 Iniciar Sesión",
                      command=ventana_iniciar_sesion,
                      bg="#A4C3B2", fg="white",
                      font=("Helvetica", 14, "bold"),
                      width=20, height=3, cursor="hand2")
btn_login.pack(pady=15)

btn_registro = tk.Button(frame_botones, text="📝 Registrarse",
                         command=ventana_registrarse,
                         bg="#6B9080", fg="white",
                         font=("Helvetica", 14, "bold"),
                         width=20, height=3, cursor="hand2")
btn_registro.pack(pady=15)

frame_derecho = tk.Frame(frame_principal, bg="#CCE3DE")
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

try:
    from PIL import Image, ImageTk

    imagen = Image.open('Dac logo png.png')
    imagen = imagen.resize((500, 500), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(frame_derecho, image=photo, bg="#CCE3DE")
    label_imagen.image = photo
    label_imagen.pack(expand=True)
except Exception as e:
    tk.Label(frame_derecho, text="\n\n🧘‍♀️\n\nDAC\n\nPILATES\n\n✨",
             font=("Helvetica", 48, "bold"),
             bg="#CCE3DE",
             fg="#6B9080").pack(expand=True)

window.mainloop()