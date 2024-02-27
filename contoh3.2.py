# Menggunakan Try untuk pengucualian jika salah memasukan inputan
try :
    # Memasukan Inputan
    bilangan = int(input("Masukan Bilangan : "))
    # Mengeksekusi
    if bilangan > 0:
        print("positif")
    elif bilangan < 0:
        print("negatif")
    elif bilangan == 0:
        print("Nol")
# Menggunakan except ValueError, jika salah memasukan inputan selain angka
except ValueError:
    print("Masukan dalam bentuk angka")