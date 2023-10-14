# Nama  :ILHAM FADILAH
# NIM   :2207009
# PBO
# TUGAS 3

class Orang():
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def getfirstname(self):
        return self.firstname
    
    def getlastname(self):
        return self.lastname

class Alamat():
    def __init__(self,jalan,kota):
        self.jalan = jalan
        self.kota = kota

class Mahasiswa(Orang):
    pass

class Mahasiswa(Orang,Alamat):
    def __init__(self, firstname, lastname,nim,jalan,kota):
        self.nim = nim

        Orang.__init__(self,firstname,lastname)
        Alamat.__init__(self,jalan,kota)

       # super().__init__(firstname, lastname)

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.nim}"

    def printdata(self):
        print(f"Nama : {self.getfirstname()} {self.lastname}")
        print(f"NIM : {self.nim}")
        print(f"Alamat : {self.jalan}, {self.kota}")

mhs = Mahasiswa("ILHAM","FADILAH","2207009","Bayongbong","Garut")
mhs.printdata()