import time

def insertion_sort(arr):
    print("\nProceso de Insertion Sort:")
    for i in range(1, len(arr)):
        valor = arr[i]
        j = i - 1
        while j >= 0 and str(valor) < str(arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
            print(f"Desplazamiento en posición {j+1}: {arr}")
            time.sleep(1)
        arr[j + 1] = valor
        print(f"Inserción de '{valor}' en posición {j+1}: {arr}")
        time.sleep(1)
    return arr