def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Contoh penggunaan:
n = int(input("Masukkan nilai n untuk deret Fibonacci: "))
fibonacci(n)