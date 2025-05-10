from ShellSortLib import shell_sort
from QuickSortLib import quicksort
from HeapSortLib import heap_sort
from RadixSortLib import radix_sort
from BurbujaLib import bubble_sort
from InsercionLib import insertion_sort
from SeleccionLib import selection_sort

print("Programa de ordenamiento por distintos métodos")
datos = input("Ingresa los elementos separados por espacios: ").split()

while True:
    print("\nMenú de métodos de ordenamiento:")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Selection Sort")
    print("4. ShellSort")
    print("5. Quicksort")
    print("6. Heapsort")
    print("7. Radix Sort")
    print("8. Salir")
    opcion = input("Seleccione una opción (1-8): ")
    copia = datos.copy()

    if opcion == '4':
        resultado = shell_sort(copia)
    elif opcion == '5':
        resultado = quicksort(copia)
    elif opcion == '6':
        resultado = heap_sort(copia)
    elif opcion == '7':
        resultado = radix_sort(copia)
    elif opcion == '1':
        resultado = bubble_sort(copia)
    elif opcion == '2':
        resultado = insertion_sort(copia)
    elif opcion == '3':
        resultado = selection_sort(copia)
    elif opcion == '8':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
        continue

    print("Resultado final:", resultado)
