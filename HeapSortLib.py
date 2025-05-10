import time

def heapify(arr, n, i, depth=0):
    indent = "  " * depth
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and str(arr[l]) > str(arr[largest]):
        largest = l
    if r < n and str(arr[r]) > str(arr[largest]):
        largest = r
    if largest != i:
        print(f"{indent}Intercambiando {arr[i]} con {arr[largest]}")
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"{indent}Estado actual: {arr}")
        time.sleep(1)
        heapify(arr, n, largest, depth + 1)

def heap_sort(arr):
    print("\nProceso de HeapSort:")
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    print("Max Heap creado:", arr)
    time.sleep(1)
    for i in range(n - 1, 0, -1):
        print(f"Intercambiando {arr[0]} con {arr[i]}")
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Estado actual: {arr}")
        time.sleep(1)
        heapify(arr, i, 0)
    return arr