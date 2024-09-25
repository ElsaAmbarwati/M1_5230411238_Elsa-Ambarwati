import math
#2D: Luas persegi panjang
print("***Perhitungan Luas Persegi Panjang 2D***")
panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))
luas_persegi_panjang = panjang * lebar
print(f"Luas persegi panjang: {luas_persegi_panjang:.2f}")

print()

#3D: Volume kerucut
print("***Perhitungan Volume Kerucut 3D***")

jari_jari_kerucut = float(input("Masukkan jari-jari kerucut: "))
tinggi_kerucut = float(input("Masukkan tinggi kerucut: "))
volume_kerucut = (1/3) * math.pi * jari_jari_kerucut**2 * tinggi_kerucut
print(f"Volume kerucut: {volume_kerucut:.2f}")