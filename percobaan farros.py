print("=== Program Hitung Rata-Rata ===")

jumlah = int(input("Berapa banyak angka? "))

total = 0

for i in range(jumlah):
    angka = float(input(f"Masukkan angka ke-{i+1}: "))
    total += angka

rata = total / jumlah

print("Total nilai:", total)
print("Rata-rata :", rata)