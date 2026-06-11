import sqlite3

class db_hry:

    def __init__(self):
        #tento connect vytvori databazu bez tabulky (ak este neexistuje)
        self.conn=sqlite3.connect("db_hry.db")
        self.cursor=self.conn.cursor()

    def vytvor_databazu(self):
        #tabulka hraci
        #tabulka inventar
    
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS hraci (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazov TEXT UNIQUE NOT NULL,
            max_zivoty INTEGER NOT NULL,
            zivoty INTEGER NOT NULL,
            utok INTEGER NOT NULL,
            iniciativa INTEGER NOT NULL,
            mana INTEGER NOT NULL,
            level INTEGER NOT NULL,
            xp INTEGER NOT NULL,
            zlato INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS inventar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hrac_id INTEGER NOT NULL,
            nazov_predmetu TEXT NOT NULL,
            typ TEXT NOT NULL,
            hodnota INTEGER NOT NULL,
            FOREIGN KEY (hrac_id) REFERENCES hraci(id) ON DELETE CASCADE
        );
        """)
        self.conn.commit()
   
    def uloz_hraca(self, hrac):
        #tabulka hraci
        #tabulka inventar
        self.cursor.execute("""
            INSERT INTO hraci(id, nazov, max_zivoty, zivoty, utok, iniciativa, mana, level, xp, zlato)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,(hrac.id, hrac.nazov, hrac.max_zivoty, hrac.zivoty, hrac.utok, hrac.iniciativa, hrac.mana, hrac.level, hrac.xp, hrac.zlato))
        self.conn.commit()
    
    def func_zavri_db(self):
        self.conn.close()