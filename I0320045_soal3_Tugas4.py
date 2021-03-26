# Mulai

# Mengimput berat dalam Kg agar mudah
# Merubah Lbs menjadi Kg
a = 0.45
b = a * 50

print("Berat max untuk 1 orang penumpang adalah ", b, "Kg")
print("Silahkan input berat barang bawaan Anda dalam Kg")
x = int(input("Masukkan berat barang bawaaan Anda : "))
if x > 22.5 :
    print("Berat barang melebihi batas maksimal :", x > 22.5,
          "Anda dapat membayar fee untuk berat lebih atau mengurangi barang bawaan Anda")
else:
    print("Berat bawaan Anda tidak melebih batas maksimal :", x > 22.5,
          "Silahkan menunggu di waiting room")

# Selesai
