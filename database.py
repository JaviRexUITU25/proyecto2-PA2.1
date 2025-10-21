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
    def __init__(self,nombre,telefono,tipo):
        super().__init__(nombre,telefono,tipo)

class Instructor(Usuario):
    def __init__(self,nombre,telefono,tipo):
        super().__init__(nombre,telefono,tipo)











