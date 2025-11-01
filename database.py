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

    def obtener_id(self):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute(
                "SELECT id_usuario FROM usuarios WHERE nombre=? AND telefono=?",
                (self.nombre, self.telefono)
            )
            fila = cur.fetchone()
            return fila["id_usuario"] if fila else None

class Sesion:
    def __init__(self,nombre,dia, hora, cupo):
        self.nombre = nombre
        self.dia= dia
        self.hora = hora
        self.cupo = cupo
    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sesiones (
                id_sesion INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT NOT NULL,
                dia TEXT NOT NULL,
                hora TEXT NOT NULL,
                cupo INTEGER NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO sesiones (nombre, dia, hora, cupo) VALUES (?,?,?,?)",
                (self.nombre,self.dia,self.hora, self.cupo)
            )
        print("Sesión registrada con éxito")

    @staticmethod
    def listar():
        with Sesion._conn() as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute("SELECT * FROM sesiones")
            return cur.fetchall()

    @staticmethod
    def eliminar(id_sesion):
        with Sesion._conn() as conn:
            conn.execute("DELETE FROM sesiones WHERE id_sesion = ?",
            (id_sesion,))
            conn.commit()
            print(f"Sesión {id_sesion} eliminada con éxito")




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
            conn.execute(
                "INSERT INTO inscripciones (id_usuario, id_sesion) VALUES (?,?)",
                (self.id_usuario, self.id_sesion)
            )
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
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute(
                "DELETE FROM inscripciones WHERe id_usuario = ? AND id_sesion = ?",
                (id_usuario,id_sesion)
            )
        conn.commit()

    @staticmethod
    def obtener_id_usuario(nombre, telefono):
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.execute("SELECT id_usuario FROM usuarios WHERE nombre=? AND telefono=?",
                               (nombre, telefono))
            fila = cur.fetchone()
            return fila["id_usuario"] if fila else None



conn = sqlite3.connect('gimnasio.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
# conn.commit()
# conn.close()
data = cursor.fetchall()
for row in data:
    print(row)
conn.close()

