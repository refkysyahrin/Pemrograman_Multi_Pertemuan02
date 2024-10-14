def evaluasi_kinerja(nilai):
    if nilai >= 90:
        print ("Sangat Baik")
    elif nilai >= 80:
        print ("Baik")
    elif nilai >= 70:
        print ("Cukup")
    elif nilai >= 60:
        print ("Rata-rata")
    else:
        print ("Kurang")

# Contoh penggunaan:
nilai = float(input("Masukkan nilai siswa: "))

kinerja = evaluasi_kinerja(nilai)

