def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def find_element(arr, target):
    try:
        index = arr.index(target)
        return index + 1
    except ValueError:
    
        return -1


data = [56, 34, 89, 15, 2, 87, 200, 23, 31, 28]

angka_cari = int(input("Angka yang di cari: "))

bubble_sort(data)
print("Setelah BubbleSort:", data)

posisi = find_element(data, angka_cari)

if posisi != -1:
    print(f"Elemen ditemukan pada posisi ke-{posisi}")
else:
    print("Elemen tidak ditemukan pada list")
