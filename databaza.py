import sqlite3

class class_db_hry:

    def __init__(self, path):
        #tento connect vytvori databazu bez tabulky (ak este neexistuje)
        #toto bude path: db_hry.db
        self.conn=sqlite3.connect(path)
        #toto zapina funkciu foreign key, ide to hned za vytvorenie db
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.cursor=self.conn.cursor()

        self.path=path

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
        #toto ide pred commit!!!
        hrac.id=self.cursor.lastrowid
        self.conn.commit()
    
    def uloz_existujuceho_hraca(self, hrac):
        #tabulka hraci (id nevkladam, to mi urobi DB (tabulka) automaticky, cize posielam o jeden parameter menej!)
        self.cursor.execute("""
            UPDATE hraci
            SET nazov=?, max_zivoty=?, zivoty=?, utok=?, iniciativa=?, mana=?, level=?, xp=?, zlato=?
            WHERE id=?
            """,(hrac.nazov, hrac.max_zivoty, hrac.zivoty, hrac.utok, hrac.iniciativa, hrac.mana, hrac.level, hrac.xp, hrac.zlato, hrac.id))
        self.conn.commit()
    
    def uloz_inventar(self, hrac):
        
        #nieco na tento styl DELETE FROM INVENTAR WHERE ID=hrac.id
        #narvat novy inventar ako nizsie (cez INSERT)
        #tabulka inventar
        for predmet in hrac.inventar:
            self.cursor.execute("""
                INSERT INTO inventar(hrac_id, nazov_predmetu, typ, hodnota, konzumovatelny)
                VALUES (?, ?, ?, ?, ?)
                """,(hrac.id, predmet.nazov, predmet.typ, predmet.hodnota, predmet.konzumovatelny))
        self.conn.commit()    

    def nacitaj_hraca(self, id_hraca):
        #tabulka hraci
        self.cursor.execute("""
            SELECT *
            FROM hraci
            WHERE id=?
        """,(id_hraca,))
        #nemusim commitovat ak selectuje
        #self.conn.commit()  toto sem nema ist!!
        #fetch skopiruje to, co je v cursore
        nacitany_hrac=self.cursor.fetchone()
        return nacitany_hrac

    def nacitaj_vsetkych_hracov(self):
        #tabulka hraci
        self.cursor.execute("""
            SELECT * FROM hraci
            """)
        nacitani_hraci=self.cursor.fetchall()
        return nacitani_hraci

    def func_zavri_db(self):
        self.conn.close()

    def func_otvor_db(self):
        self.conn=sqlite3.connect(self.path)
        self.cursor=self.conn.cursor()