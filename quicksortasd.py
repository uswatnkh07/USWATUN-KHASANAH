import random
import os
os.system('cls')

print("========================================================================")
print("======================= IMPLEMENTASI QUICK SORT ========================")
print("===================== MENGGUNAKAN LIBRARY RANDOM =======================")
print("")

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = []
        equal = []
        right = []
        for num in arr:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                right.append(num)
        return quick_sort(left) + equal + quick_sort(right)
    
# Menghasilkan daftar bilangan bulat acak
arr = [random.randint(1, 50) for i in range(11)]

# Menampilkan daftar bilangan bulat acak
print("DAFTAR YANG BELUM DIURUTKAN:", arr)

# Mengurutkan daftar bilangan
quick_sort(arr)

# Menampilkan daftar bilangan bulat yang sudah terurut
print("DAFTAR YANG SUDAH DIURUTKAN:", quick_sort(arr))
print("")
print("====================== TERIMAKASIH TELAH MENCOBA ========================")
