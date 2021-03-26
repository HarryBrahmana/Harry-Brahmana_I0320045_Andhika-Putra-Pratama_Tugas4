# Mulai
# Menghitung berapa kali angka kedua dapat dibagi menjadi angka pertama
print("Menghitung Operation Floor")
print("Note : Output dari program ini adalah berapa kali angka kedua dapat dibagi menjadi angka pertama ")

x = int(input("Masukkan data bilangan bulat pertama : "))
y = int(input("Masukkan data bilangan bulat kedua : "))

print("Angka pertama kamu adalah :", x,
      "Angka kedua kamu adalah :", y)
op_floor = x // y
print("Hasil perhitungan adalah : ")
print("Angka pertama yang kamu input hanya dapat dibagi sebanyak :", op_floor, "kali oleh angka kedua")

b = str(input("Ketik 'Yes' jika kmau menyukai program ini: "))
if b == 'Yes' :
    print("Terima Kasih")
else:
    input("Klik enter untuk selesai :")

# Selesai