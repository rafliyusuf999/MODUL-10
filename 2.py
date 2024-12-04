def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1 

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 

data = [10, 25, 37, 48, 59, 72, 84, 96]  
target = 37

result_linear = linear_search(data, target)
print("Linear Search:")
if result_linear != -1:
    print(f"Elemen {target} ditemukan pada indeks {result_linear}.")
else:
    print(f"Elemen {target} tidak ditemukan.")

result_binary = binary_search(data, target)
print("\nBinary Search:")
if result_binary != -1:
    print(f"Elemen {target} ditemukan pada indeks {result_binary}.")
else:
    print(f"Elemen {target} tidak ditemukan.")
