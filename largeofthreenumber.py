def angka_terbesar(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Contoh penggunaan:
num1 = int(input("Masukkan angka pertama: "))
num2 = int(input("Masukkan angka kedua: "))
num3 = int(input("Masukkan angka ketiga: "))
terbesar=angka_terbesar(num1, num2, num3)
print(f"Angka terbesar adalah:", terbesar)

