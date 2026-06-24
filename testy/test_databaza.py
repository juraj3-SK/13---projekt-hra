import sqlite3
import pytest

from databaza import class_db_hry
from predmet import class_Predmet

class TestHrac:
    def __init__(self, meno_hraca="test_hrac"):
        self.id = None
        self.nazov = meno_hraca
        self.max_zivoty = 100
        self.zivoty = 80
        self.utok = 15
        self.iniciativa = 10
        self.mana = 30
        self.level = 2
        self.xp = 5
        self.zlato = 50

        self.inventar = [
            class_Predmet("Mec", "zbran", 10, 0),
            class_Predmet("Maly lektvar", "heal", 20, 1),
            class_Predmet("Mana elixir", "mana", 30, 1)
        ]

#vyrobi vzdy cistu databazu
@pytest.fixture
def db(tmp_path):
    cesta_db = tmp_path / "test_db_hry.db"

    databaza = class_db_hry(str(cesta_db))
    databaza.vytvor_databazu()

    yield databaza

    databaza.func_zavri_db()

#test na to, ci tabulke su dobre vytvorene
def test_vytvor_tabulky(db):
    db.cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='hraci'
    """)
    tabulka_hraci = db.cursor.fetchone()

    db.cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='inventar'
    """)
    tabulka_inventar = db.cursor.fetchone()

    assert tabulka_hraci is not None
    assert tabulka_inventar is not None

def test_uloz_hraca(db):
    hrac=TestHrac()
    db.uloz_hraca(hrac)

    #otestujem, ci ma hrac ID
    assert hrac.id is not None

    #toto vreacia stlpce, nie objekt!!
    nacitany_hrac=db.nacitaj_hraca(hrac.id)

    assert nacitany_hrac==(
        hrac.id,
        "test_hrac",
        100,
        80,
        15,
        10,
        30,
        2,
        5,
        50
        )

def test_nacitaj_nula_hracov(db):
    nacitani_hraci=db.nacitaj_vsetkych_hracov()
    #skumam ci je zoznam prazdny (a.k.a. ma nulovu dlzku)
    assert (len(nacitani_hraci)==0)
    #alebo este inak povedane to iste co hore, ci je zoznam prazdny
    #pre istotu nechavam obe, ak by nastal nejaky patologicky pripad, ze jeden assert zbehne a druhy nie
    assert (nacitani_hraci==[])

def test_nacitaj_jedneho_hraca(db):
    hrac=TestHrac()
    db.uloz_hraca(hrac)
    nacitani_hraci=db.nacitaj_vsetkych_hracov()
    #skumam ci je zoznam prazdny (a.k.a. ma nulovu dlzku)
    assert (len(nacitani_hraci)==1)
    assert nacitani_hraci==[(
        hrac.id,
        "test_hrac",
        100,
        80,
        15,
        10,
        30,
        2,
        5,
        50
    )]

def test_nacitaj_viac_hracov(db):
    hraci=[TestHrac("th1"), TestHrac("th2"), TestHrac("th3")]
    for hrac in hraci:
        db.uloz_hraca(hrac)

    nacitani_hraci=db.nacitaj_vsetkych_hracov()
    
    assert (len(nacitani_hraci)==3)
    
    for i, hrac in enumerate(hraci):
        assert nacitani_hraci[i]==(
        hrac.id,
        hrac.nazov,
        100,
        80,
        15,
        10,
        30,
        2,
        5,
        50
        )