import sqlite3

class BibliotecaCarti():

    def __init__(self, db):
        self.db = db

    def init_db(self):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS carti (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titlu TEXT NOT NULL,
                autor TEXT NOT NULL,
                editura TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def read_all(self):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM carti ORDER BY titlu,autor,editura,id')
        lista = cursor.fetchall()
        conn.close()
        return lista

    def create(self, titlu, autor, editura):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO carti(titlu,autor,editura) VALUES(?,?,?)',(titlu,autor,editura))
        conn.commit()
        conn.close()
        return True

    def read_one(self, id):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM carti WHERE id=?',(id,))
        rezultat  = cursor.fetchone()
        conn.close()
        return rezultat

    def update(self ,id ,titlu, autor, editura):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('UPDATE carti SET titlu=?, autor=?, editura=? WHERE id=?', (titlu,autor,editura,id))
        conn.commit()
        conn.close()
        return True

    def delete(self, id):
        conn   = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM carti WHERE id=?', (id,))
        conn.commit()
        conn.close()
        return True
    