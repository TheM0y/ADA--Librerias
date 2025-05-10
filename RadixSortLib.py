import time

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 256
    print(f"Contando con exp={exp}")
    for i in range(n):
        index = ord(str(arr[i])[-exp]) if exp <= len(str(arr[i])) else 0
        count[index] += 1
    print("Conteo:", count)
    time.sleep(1)
    for i in range(1, 256):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = ord(str(arr[i])[-exp]) if exp <= len(str(arr[i])) else 0
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
    print(f"Resultado parcial con exp={exp}: {arr}")
    time.sleep(1)

def radix_sort(arr):
    print("\nProceso de Radix Sort:")
    if not arr:
        return arr
    max_len = max(len(str(x)) for x in arr)
    for exp in range(1, max_len + 1):
        counting_sort_for_radix(arr, exp)
    return arr