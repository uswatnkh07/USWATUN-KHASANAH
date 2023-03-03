import random
import os
os.system ('cls')
print("======================================================================")
print("====================== IMPLEMENTASI MERGE SORT =======================")
print("==================== MENGGUNAKAN LIBRARY RANDOM ======================")
print("")

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        setengah_kanan = arr[:mid]
        setengah_kiri = arr[mid:]

        merge_sort(setengah_kanan)
        merge_sort(setengah_kiri)

        i = j = k = 0

        while i < len(setengah_kanan) and j < len(setengah_kiri):
            if setengah_kanan[i] < setengah_kiri[j]:
                arr[k] = setengah_kanan[i]
                i += 1
            else:
                arr[k] = setengah_kiri[j]
                j += 1
            k += 1

        while i < len(setengah_kanan):
            arr[k] = setengah_kanan[i]
            i += 1
            k += 1

        while j < len(setengah_kiri):
            arr[k] = setengah_kiri[j]
            j += 1
            k += 1


# Menghasilkan daftar bilangan bulat acak
arr = [random.randint(1, 50) for i in range(11)]

# Menampilkan daftar bilangan bulat acak
print("DAFTAR YANG BELUM DIURUTKAN:", arr)

# Mengurutkan daftar bilangan
merge_sort(arr)

# Menampilkan daftar bilangan bulat yang sudah terurut
print("DAFTAR YANG SUDAH DIURUTKAN:", arr)
print("")
print("===================== TERIMAKASIH TELAH MENCOBA ======================")