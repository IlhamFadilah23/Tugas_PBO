kalimat = "ini adalah kalimat"
paragraf = """ini adalah paragraf,
paragraf terdiri beberapa baris."""
print(kalimat)
print(paragraf)

kalimat = "abcdefghijklmnopqrstuvwxyz"
print(kalimat[:5])
print(kalimat[5:10])
print(kalimat[21:])
print(kalimat[-10:-1])
print(kalimat[-10:])

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

kalimat = "Hallo, Semua.Saya adalah programer Python."
tambahan = "Saya sedang belajar Python. Mohon bimbingannya"
print(kalimat + tambahan)

kalimat = "Halo semua. Saya adalah programer \"Python\". "
tambahan = "Saya sedang belajar \"Python\". Mohon bimbingannya. "
print(kalimat + tambahan)

umur = 21
rumah = 3
mobil = 5
emas = 10
kalimat = "Saya berumur {} tahun, rumah saya ada {}, mobil saya ada {}, dan emas saya ada {} kilogram"
print(kalimat.format(umur,rumah,mobil,emas))