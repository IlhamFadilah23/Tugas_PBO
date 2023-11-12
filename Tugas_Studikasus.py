# Nama    : Ilham Fadilah
# Nim     : 2207009

class Karyawan:
    def __init__(self, nama):
        self.nama = nama
        self.gaji_pokok = 4000000
        self.uang_makan_harian = 30000

    def hitung_gaji(self):
        pass


class Manager(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.uang_tunjangan_profesi = 1500000
        self.uang_transport_harian = 30000

    def hitung_gaji(self):
        return self.gaji_pokok + (self.uang_makan_harian * 30) + (self.uang_transport_harian * 30) + self.uang_tunjangan_profesi


class Admin(Karyawan):
    def __init__(self, nama, jam_lembur=0):
        super().__init__(nama)
        self.uang_transport_harian = 15000
        self.jam_lembur = jam_lembur
        self.uang_lembur_per_jam = 40000

    def hitung_gaji(self):
        return self.gaji_pokok + (self.uang_makan_harian * 30 ) + (self.uang_transport_harian * 30) + (self.jam_lembur * self.uang_lembur_per_jam)


class Marketing(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.uang_transport_harian = 50000

    def hitung_gaji(self):
        return self.gaji_pokok + (self.uang_makan_harian * 30) + (self.uang_transport_harian * 30)


def main():
    # Membuat objek karyawan
    karyawan1 = Manager("Asep")
    karyawan2 = Admin("Dadang", 20)
    karyawan3 = Marketing("Ujang")

    # Menghitung dan menampilkan gaji karyawan
    print(f"Gaji {karyawan1.nama}: {karyawan1.hitung_gaji()} rupiah")
    print(f"Gaji {karyawan2.nama}: {karyawan2.hitung_gaji()} rupiah")
    print(f"Gaji {karyawan3.nama}: {karyawan3.hitung_gaji()} rupiah")


main()
