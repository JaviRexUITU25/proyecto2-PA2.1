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


class Sesion():
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
            cur = conn.execute("SELECT * FROM sesiones")
            filas = cur.fetchall()
            if not filas:
                print("No hay sesiones registradas")
                return
            print("Listado de sesiones")
            for f in filas:
                print(f"ID: {f['id_sesion']} | Nombre: {f['nombre']} | Dia: {f['dia']} | Hora: {f['hora']} | Cupo : {f['Cupo']}")
    @staticmethod
    def eliminar():
        with Sesion._conn() as conn:
            cur = conn.execute("DELETE FROM sesiones WHERE ")


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
def verificar_usuario_existente(nombre,telefono):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            "SELECT id_usuario FROM usuarios WHERE nombre = ? AND telefono = ?",
            (nombre,telefono)
        )
        return cur.fetchone() is not None


conn = sqlite3.connect('gimnasio.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")
# conn.commit()
# conn.close()
data = cursor.fetchall()
for row in data:
    print(row)
conn.close()
def obtener_id(nombre,telefono):
    conn = sqlite3.connect('gimnasio.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id_usuario FROM usuarios WHERE nombre = ? AND telefono = ?")
    data = cursor.fetchall()
#     for row in data:
#         print(row)
#     conn.close()
Sesion.listar()