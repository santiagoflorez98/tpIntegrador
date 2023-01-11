import psycopg2
class database():
    def __init__(self):
        self.conn = psycopg2.connect("dbname= TPGAD user=postgres password=321")
        self.cur = self.conn.cursor()
    def desconectar_db(self):
        self.cur = self.cur.close()
        self.conn = self.conn.close()
    def crear_tabla(self):
        self.cur.execute("CREATE TABLE vectores (id serial PRIMARY KEY, vector double precision[] , ruta varchar, idHoja bigint);")
        self.conn.commit()
    def consulta_ver(self):
        self.cur.execute("SELECT * FROM vectores WHERE vectores.id=13")
        record = self.cur.fetchall()
        for r in record:
            print(r)
    def consulta_cargar(self,vec,ruta):
        self.cur.execute("INSERT INTO vectores(vector,ruta) VALUES (%s, %s)", (vec, ruta))
        self.conn.commit()

