import time

def shell_sort(arr):
    print("\nProceso de ShellSort:")
    n = len(arr)
    gap = n // 2
    while gap > 0:
        print(f"Gap: {gap}")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and str(arr[j - gap]) > str(temp):
                arr[j] = arr[j - gap]
                j -= gap
                print(f"Moviendo {arr[j]} a la posición {j + gap}: {arr}")
                time.sleep(1)
            arr[j] = temp
            print(f"Insertado {temp} en la posición {j}: {arr}")
            time.sleep(1)
        gap //= 2
    return arr