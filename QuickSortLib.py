import time
def quicksort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    print(f"{indent}Pivot: {pivot}")
    time.sleep(1)
    left = [x for x in arr if str(x) < str(pivot)]
    print(f"{indent}Izquierda: {left}")
    time.sleep(1)
    middle = [x for x in arr if str(x) == str(pivot)]
    print(f"{indent}Centro: {middle}")
    time.sleep(1)
    right = [x for x in arr if str(x) > str(pivot)]
    print(f"{indent}Derecha: {right}")
    time.sleep(1)
    return quicksort(left, depth + 1) + middle + quicksort(right, depth + 1)