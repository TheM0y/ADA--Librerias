import time

def bubble_sort(arr):
    print("\nProceso de Bubble Sort:")
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if str(arr[j]) > str(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Intercambio en posición {j} y {j+1}: {arr}")
                time.sleep(1)
    return arr