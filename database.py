import sqlite3
DB_NAME = "gimnasio.db"
class Usuario:
    def __init__(self,nombre,telefono,tipo):
        self.nombre= nombre
        self.telefono = telefono
        self.tipo  = tipo
    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                tipo TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO usuarios (nombre, telefono, tipo) VALUES (?,?,?)",
                (self.nombre,self.telefono, self.tipo)
            )
        print(f"Usuario: {self.nombre} registrado con éxito")

    def verificar_usuario_existente(nombre, telefono):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute(
                "SELECT id_usuario FROM usuarios WHERE nombre = ? AND telefono = ?",
                (nombre, telefono)
            )
            return cur.fetchone() is not None

    @staticmethod
    def verificar_inicio_sesion(codigo, telefono):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            "SELECT * FROM usuarios WHERE id_usuario=? AND telefono=?",
            (codigo, telefono)
        )
        usuario = cur.fetchone()
        conn.close()
        return dict(usuario)

    def obtener_id(self):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute(
                "SELECT id_usuario FROM usuarios WHERE nombre=? AND telefono=?",
                (self.nombre, self.telefono)
            )
            fila = cur.fetchone()
            return fila["id_usuario"] if fila else None

    @staticmethod
    def obtener_por_codigo_y_telefono(codigo, telefono):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute(
                "SELECT nombre FROM usuarios WHERE id_usuario=? AND telefono=?",
                (codigo, telefono)
            )
            fila = cur.fetchone()
            return fila["nombre"] if fila else None

    @staticmethod
    def recuperar_codigo(nombre, telefono):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute(
                "SELECT id_usuario FROM usuarios WHERE nombre=? AND telefono=?",
                (nombre, telefono)
            )
            fila = cur.fetchone()
            return fila["id_usuario"] if fila else None
class Sesion:
    def __init__(self,nombre,id_horario, cupo):
        self.nombre = nombre
        self.id_horario = id_horario
        self.cupo = cupo
    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sesiones (
                id_sesion INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT NOT NULL,
                id_horario INTEGER NOT NULL,
                cupo INTEGER NOT NULL,
                FOREIGN KEY (id_horario) REFERENCES horarios(id_horario)
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO sesiones (nombre, id_horario, cupo) VALUES (?,?,?)",
                (self.nombre,self.id_horario, self.cupo)
            )
        print("Sesión registrada con éxito")

    @staticmethod
    def listar():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.execute("""
                    SELECT sesiones.id_sesion, sesiones.nombre, sesiones.cupo,
                           horarios.dia, horarios.hora_inicio, horarios.hora_fin
                    FROM sesiones
                    INNER JOIN horarios 
                    ON sesiones.id_horario = horarios.id_horario
                """)
        return cur.fetchall()

    @staticmethod
    def eliminar(id_sesion):
        with Sesion._conn() as conn:
            conn.execute("DELETE FROM sesiones WHERE id_sesion = ?",
            (id_sesion,))
            conn.commit()
            print(f"Sesión {id_sesion} eliminada con éxito")

    @staticmethod
    def disminuir_cupo(id_sesion):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "UPDATE sesiones SET cupo = cupo - 1 WHERE id_sesion = ? AND cupo > 0",
                (id_sesion,)
            )
            conn.commit()

    @staticmethod
    def aumentar_cupo(id_sesion):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "UPDATE sesiones SET cupo = cupo + 1 WHERE id_sesion = ?",
                (id_sesion,)
            )
            conn.commit()
class Inscripcion:
    def __init__(self,id_usuario, id_sesion):
        self.id_usuario = id_usuario
        self.id_sesion = id_sesion

    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS inscripciones (
            id_inscripcion INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_usuario INTEGER NOT NULL,
            id_sesion INTEGER NOT NULL, 
            FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
            FOREIGN KEY(id_sesion) REFERENCES sesiones(id_sesion)
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            cur = conn.execute("SELECT cupo FROM sesiones WHERE id_sesion = ?", (self.id_sesion,))
            fila = cur.fetchone()
            if fila and fila["cupo"] > 0:
                conn.execute(
                    "INSERT INTO inscripciones (id_usuario, id_sesion) VALUES (?, ?)",
                    (self.id_usuario, self.id_sesion)
                )
                conn.commit()
                Sesion.disminuir_cupo(self.id_sesion)
        print("Inscripción registrada con exito")

    @staticmethod
    def listar_por_usuario(id_usuario):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.execute("""
            SELECT sesiones.*
            FROM inscripciones
            INNER JOIN sesiones ON inscripciones.id_sesion = sesiones.id_sesion
            WHERE inscripciones.id_usuario = ?
        """, (id_usuario,))
        return cur.fetchall()

    @staticmethod
    def eliminar_inscripcion(id_usuario, id_sesion):
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute(
                "DELETE FROM inscripciones WHERE id_usuario=? AND id_sesion=?",
                (id_usuario, id_sesion)
            )
        Sesion.aumentar_cupo(id_sesion)
        conn.commit()

    @staticmethod
    def obtener_id_usuario(nombre, telefono):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute("SELECT id_usuario FROM usuarios WHERE nombre=? AND telefono=?",
                               (nombre, telefono))
            fila = cur.fetchone()
            return fila["id_usuario"] if fila else None

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin):
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS horarios (
                id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
                dia TEXT NOT NULL,
                hora_inicio TEXT NOT NULL,
                hora_fin TEXT NOT NULL
            )
        """)
        conn.commit()
        return conn
    def guardar(self):
        conn = sqlite3.connect(DB_NAME)
        with conn:
            conn.execute(
                "INSERT INTO horarios (dia, hora_inicio, hora_fin) VALUES (?, ?, ?)",
                (self.dia, self.hora_inicio, self.hora_fin)
            )

    @staticmethod
    def listar():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.execute("SELECT * FROM horarios")
        return cur.fetchall()

    @staticmethod
    def obtener(id_horario):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cur = conn.execute("SELECT * FROM horarios WHERE id_horario=?", (id_horario,))
        return cur.fetchone()


conn = sqlite3.connect('gimnasio.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM sesiones")
# conn.commit()
# conn.close()
data = cursor.fetchall()
for row in data:
    print(row)
conn.close()


