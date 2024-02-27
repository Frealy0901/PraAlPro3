# Menggunakan Try untuk pengucualian jika salah memasukan inputan
try:
    # Memasukan Inputan
    sisia = int(input("Masukan sisi 1: "))
    sisib = int(input("Masukan sisi 2: "))
    sisic = int(input("Masukan sisi 3: "))
    # Mengeksekusi
    if sisia == sisib == sisic:
        print("Ketiga isi sama")
    elif sisia >= sisib or sisib >= sisic :
        print("2 sisi yang sama")
        # Jika pengguna memasukan  sisi yang tidak sama
    else:
        print("Tidak ada yang sama")
# Menggunakan except ValueError, jika salah memasukan inputan selain angka
except ValueError:
    print("tidak valid")