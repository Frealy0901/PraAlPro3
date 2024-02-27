# Menggunakan Try untuk pengucualian jika salah memasukan inputan
try : 
    # Memasukan Inputan  
    suhu = int(input("Suhu tubuh anda : "))
    # Mengeksekusi
    if suhu >= 38 :
        print("Anda Demam")
    else :
        print("Suhu anda Normal")
# Menggunakan except ValueError, jika salah memasukan inputan selain angka
except ValueError: 
        print("Inputan Error")