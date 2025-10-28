import math
from shapes import (
    luas_persegi, luas_persegi_panjang, luas_segitiga, luas_lingkaran
)

def test_luas_persegi():
    assert luas_persegi(4) == 16

def test_luas_persegi_panjang():
    assert luas_persegi_panjang(4, 2) == 8

def test_luas_segitiga():
    assert luas_segitiga(4, 2) == 4.0

def test_luas_lingkaran():
    assert math.isclose(luas_lingkaran(7), 153.938, rel_tol=1e-3)
