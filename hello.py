kalimat = "ini adalah kalimat"
paragraf = """ini adalah paragraf,
paragraf terdiri beberapa baris."""
print(kalimat)
print(paragraf)
#ini adalah kalimat
#ini adalah paragraf, 
#paragraf terdiri beberapa baris.

kalimat = "abcdefghijklmnopqrstuvwxyz"
print(kalimat[:5])
print(kalimat[5:10])
print(kalimat[21:])
print(kalimat[-10:-1])
print(kalimat[-10:])
#abcde
#fghij
#vwxyz
#qrstuvwxy
#qrstuvwxyz

kalimat = "Halo, semua. Saya adalah programer python"
print(kalimat.upper())
print(kalimat.lower())
print(kalimat.capitalize())
print(kalimat.title())
print(kalimat.swapcase())
print(kalimat.replace("Python", "Java"))
print(kalimat.replace("a", "i"))
print(kalimat.strip())
print(kalimat.split('.'))
#HALO, SEMUA. SAYA ADALAH PROGRAMER PYTHON
#halo, semua. saya adalah programer python
#Halo, semua. saya adalah programer python
#Halo, Semua. Saya Adalah Programer Python
#hALO, SEMUA. sAYA ADALAH PROGRAMER PYTHON
#Halo, semua. Saya adalah programer python
#Hilo, semui. Siyi idilih progrimer python
#Halo, semua. Saya adalah programer python
#['Halo, semua', ' Saya adalah programer python']

kalimat = "Hallo, Semua.Saya adalah programer Python."
tambahan = "Saya sedang belajar Python. Mohon bimbingannya"
print(kalimat + tambahan)
#Hallo, Semua.Saya adalah programer Python.Saya sedang belajar Python. Mohon bimbingannya

kalimat = "Halo semua. Saya adalah programer \"Python\". "
tambahan = "Saya sedang belajar \"Python\". Mohon bimbingannya. "
print(kalimat + tambahan)
#Halo semua. Saya adalah programer "Python". Saya sedang belajar "Python". Mohon bimbingannya.

umur = 21
rumah = 3
mobil = 5
emas = 10
kalimat = "Saya berumur {} tahun, rumah saya ada {}, mobil saya ada {}, dan emas saya ada {} kilogram"
print(kalimat.format(umur,rumah,mobil,emas))
#Saya berumur 21 tahun, rumah saya ada 3, mobil saya ada 5, dan emas saya ada 10 kilogram