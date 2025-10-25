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
    


class Cliente(Usuario):
    def __init__(self,nombre,telefono,tipo):
        super().__init__(nombre,telefono,tipo)
    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
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
                "INSERT INTO clientes (nombre, telefono, tipo) VALUES (?,?,?)",
                (self.nombre,self.telefono, self.tipo)
            )
        print(f"Usuario: {self.nombre} registrado con éxito")

class Instructor(Usuario):
    def __init__(self,nombre,telefono,tipo):
        super().__init__(nombre,telefono,tipo)
    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS instructores (
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
                "INSERT INTO instructores (nombre, telefono, tipo) VALUES (?,?,?)",
                (self.nombre,self.telefono, self.tipo)
            )
        print(f"Usuario: {self.nombre} registrado con éxito")

class sesiones():
    def __init__(self,dia, hora):
        self.dia= dia
        self.hora = hora

    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sesiones (
                id_sesion INTEGER PRIMARY KEY AUTOINCREMENT, 
                dia TEXT NOT NULL,
                hora TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO sesiones (dia, hora) VALUES (?,?)",
                (self.dia,self.hora)
            )
        print("Sesión registrada con éxito")
Usuario("Juan",2223556,"Instructor").guardar()