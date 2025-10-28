import math

def luas_persegi(sisi: float) -> float:
    return sisi * sisi

def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    return panjang * lebar

def luas_segitiga(alas: float, tinggi: float) -> float:
    return 0.5 * alas * tinggi

def luas_lingkaran(jari_jari: float) -> float:
    return math.pi * jari_jari * jari_jari
