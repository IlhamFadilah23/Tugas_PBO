import math

class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return math.pi * self.jari_jari ** 2

def Printhasil(bangun_ruang, nama, param):
    luas = bangun_ruang.hitung_luas()
    print(f"aku adalah {nama}")
    print(f"Luas {nama} dengan {param} adalah {luas}")

def main():
    persegi = Persegi(4)
    lingkaran = Lingkaran(7)

    Printhasil(persegi, "persegi", f"sisi {persegi.sisi}")
    Printhasil(lingkaran, "lingkaran", f"jari-jari {lingkaran.jari_jari}")


main()
