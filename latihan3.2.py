# Memasukan Inputan
a = int(input("Masukan bilangan pertama: "))
b = int(input("Masukan bilangan pertama: "))
c = int(input("Masukan bilangan pertama: "))

# Menggunakan ternary operator
if a > b and a > c: print("Terbesar :", a) 
elif b > a and b > c: print("Terbesar :", b)
elif c > a and c > b: print("Terbesar :", c)