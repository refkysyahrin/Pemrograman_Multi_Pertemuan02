def angka_ganjil(n):
    for i in range(1, n + 1, 2):
        print(i, end=' ')
    print()

# Contoh penggunaan:
n = int(input("Masukkan nilai n untuk mencetak angka ganjil: "))
angka_ganjil(n)
3