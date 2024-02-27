# Menggunakan Try untuk pengucualian jika salah memasukan inputan
try :
    # Memasukan Inputan
    a = int(input("Bilangan pertama : "))
    b = int(input("Bilangan pertama : "))
    c = int(input("Bilangan pertama : "))  
    # Mengeksekusi
    if a > b and a > c:
        print("Terbesar : ", a)
    if b > a and b > c:
        print("Terbesar : ", b)
    if c > a and c > b:
        print("Terbesar : ", c)
# Menggunakan except ValueError, jika salah memasukan inputan selain angka
except ValueError :
    print("Tolong masukan dalam bentuk angka")
        