# Menggunakan Try untuk pengucualian jika salah memasukan inputan
try :
    # Memasukan Inputan
    bulan = int(input("Masukan bulan(1-12): "))
    # Mengeksekusi
    if bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12:
        print(31)
    elif bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11:
        print(30)
    elif bulan == 2:
        print(29)
    # Jika pengguna memasukan  > 12 atau < 1
    else:
        print("tidak valid")
# Menggunakan except ValueError, jika salah memasukan inputan selain angka
except ValueError :
    print("Masukan dalam bentuk angka")


# jan = 31
# feb = 29
# mar = 31
# apr = 30
# mei = 31
# jun = 30
# jul = 31
# agu = 31
# sep = 30
# okt = 31
# nov = 30
# des = 31