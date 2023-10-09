#NAMA   :Ilham Fadilah
#NIM    :2207009


class x:
    x = 5

k = x()
print(k.x)

class x:
    x = 5

k = x()
k.x = 10
print(k.x)

class x:
    x=5

#k = x()
#del k.x
#print (k.x)

class mahasiswa:
    def __init__(self,nama,nim,umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

    def __str__(self):
        return f"Nama saya adalag {self.nama}, dan NIM saya adalah {self.nim}"

    def tahunlahir(self):
        return 2023 - self.umur

saya = mahasiswa("Ilham", "2207009",20)
print(saya)
print("Nama saya adalah",saya.nama)
print("NIM saya adalah",saya.nim)
print("Tahun lahir saya adalah", saya.tahunlahir())
print("Saya angkatan 20",saya.nim[0:2])