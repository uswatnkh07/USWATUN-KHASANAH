import random
import os
os.system('cls')
print("======================================================================")
print("====================== IMPLEMENTASI SHELL SORT =======================")
print("==================== MENGGUNAKAN LIBRARY RANDOM ======================")
print("")

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Menghasilkan daftar bilangan bulat acak
arr = [random.randint(1, 50) for i in range(11)]

# Menampilkan daftar bilangan bulat acak
print("DAFTAR YANG BELUM DIURUTKAN:", arr)

# Mengurutkan daftar bilangan
shell_sort(arr)

# Menampilkan daftar bilangan bulat yang sudah terurut
print("DAFTAR YANG SUDAH DIURUTKAN:", arr)
print("")
print("===================== TERIMAKASIH TELAH MENCOBA ======================")
