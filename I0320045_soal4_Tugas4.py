# Mulai

# Untuk mendaftar kursus online siswa harus berusia minimal 21 tahun dan sudah lulus ujian kualifikasi
print("uji kesesuaian pendaftar kursus online")

# Usia
usia = int(input("berapa usia kamu? "))
print(usia >= 21)

# Kelulusan ujian
lulus = str(input("Apakah kamu sudah lulus ujian kualifikasi? (lulus/belum"))

if usia >= 21 and lulus == "lulus":
    print("Anda dapat mendaftar di kursus ini")
else:
    print("Anda tidak dapat mendaftar di kursus ini")

# Selesai