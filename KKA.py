a=3
print(type(a))
print("hallo python")

b=3.5
print(type(b))

nama="moreno"
print(type(nama))

angka=[1,2,3,4,5]
print(type(angka))
angka.append(6)
print(angka)




penjualan=['beras', 'minyak', 'telur']
print(type(penjualan))
penjualan.append("gula")
penjualan.append("kopi")






for item in penjualan:
    print(item)
    
    harga = {
    "beras": 12000,
    "minyak": 17000,
    "telur": 24000,
    "gula": 15000,
    "kopi": 20000
}
    total = sum(harga.values())
print("Total harga belanja:", total)






import math

def lingkaran(r):
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    return luas, keliling

r = int(input("Masukkan Jari Jari: "))
luas, kel = lingkaran(r)
print(f"Jari-jari = {r}")
print("Luas lingkaran:", luas)
print("Keliling lingkaran:", kel)






usia = int(input("Masukkan usia: "))

if usia >= 0 and usia <= 13:
    print("Anak")
elif usia >= 14 and usia <= 24:
    print("Remaja")
elif usia >= 25 and usia <= 49:
    print("Dewasa")
elif usia >= 50:
    print("Lansia")
else:
    print("Usia tidak valid")