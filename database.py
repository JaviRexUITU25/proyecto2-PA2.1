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
            CREATE TABLE IF NOT EXISTS usuario (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO usuarios (nombre, telefono) VALUES (?,?,?)",
                (self.nombre,self.telefono)
            )
        print(f"Usuario: {self.nombre} registrado con éxito")
    


class Cliente(Usuario):
    def __init__(self,nombre,telefono,tipo = "Cliente"):
        super().__init__(nombre,telefono,tipo)
    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO cliente (nombre, telefono) VALUES (?,?,?)",
                (self.nombre,self.telefono)
            )
        print(f"Usuario: {self.nombre} registrado con éxito")

class Instructor(Usuario):
    def __init__(self,nombre,telefono,tipo = "Instructor"):
        super().__init__(nombre,telefono,tipo)
    def _conn(self):
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory= sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS instructor (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT, 
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn
    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO instructor (nombre, telefono) VALUES (?,?,?)",
                (self.nombre,self.telefono)
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
                "INSERT INTO sesiones (dia, hora) VALUES (?,?,?)",
                (self.dia,self.hora)
            )
        print(f"Usuario: {self.nombre} registrado con éxito")








