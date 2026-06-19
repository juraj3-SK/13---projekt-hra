import sqlite3

class db_hry:

    def __init__(self):
        #tento connect vytvori databazu bez tabulky (ak este neexistuje)
        self.conn=sqlite3.connect("db_hry.db")
        #toto zapina funkciu foreign key, ide to hned za vytvorenie db
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor=self.conn.cursor()

    def vytvor_databazu(self):
        #tabulka hraci
        #tabulka inventar
    
        #pouzijem execute script ak dam viac prikazov naraz (napr. vytvaram dve tabulky)
        #self.cursor.executescript("""
        #alebo to urobim cez "execute", ale po jednom prikaze (napr.  vyrobenie dvoch tabuliek = 2x execute)
        #commit na konci je len jeden
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
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hrac_id INTEGER NOT NULL,
            nazov_predmetu TEXT NOT NULL,
            typ TEXT NOT NULL,
            hodnota INTEGER NOT NULL,
            konzumovatelny INTEGER NOT NULL,
            FOREIGN KEY (hrac_id) REFERENCES hraci(id) ON DELETE CASCADE
        );
        """)
        self.conn.commit()
   
    def uloz_hraca(self, hrac):
        #tabulka hraci (id nevkladam, to mi urobi DB (tabulka) automaticky, cize posielam o jeden parameter menej!)
        self.cursor.execute("""
            INSERT INTO hraci(nazov, max_zivoty, zivoty, utok, iniciativa, mana, level, xp, zlato)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,(hrac.nazov, hrac.max_zivoty, hrac.zivoty, hrac.utok, hrac.iniciativa, hrac.mana, hrac.level, hrac.xp, hrac.zlato))
        self.conn.commit()
    
    def uloz_inventar(self, hrac):
        #tabulka inventar
        for predmet in hrac.inventar:
            self.cursor.execute("""
                INSERT INTO inventar(hrac_id, nazov_predmetu, typ, hodnota, konzumovatelny)
                VALUES (?, ?, ?, ?, ?)
                """,(hrac.id, predmet.nazov, predmet.typ, predmet.hodnota, predmet.konzumovatelny))
            self.conn.commit()

    def func_zavri_db(self):
        self.conn.close()