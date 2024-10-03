# Implementación optimizada del algoritmo de ordenamiento por burbuja (Bubble Sort)
def bubbleSort(arr):
    n = len(arr)  # Determina el tamaño del arreglo
    
    # Recorre todos los elementos del arreglo
    for i in range(n):
        swapped = False  # Marca si ocurrió algún intercambio en esta pasada
        
        # Recorre desde el inicio hasta el penúltimo elemento que aún no está ordenado
        for j in range(0, n-i-1):
            
            # Compara el elemento actual con el siguiente
            if arr[j] > arr[j+1]:
                # Si el actual es mayor, intercambia ambos
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Indica que ocurrió un intercambio
        
        # Si no hubo intercambios en la pasada, el arreglo ya está ordenado
        if not swapped:
            break  # Termina el bucle, ya que no es necesario seguir verificando

# Código de prueba
if __name__ == "__main__":
    # Arreglo de ejemplo a ordenar (cambiado)
    arr = [14, 7, 23, 5, 12, 9, 4, 6]

    # Llama a la función de ordenamiento por burbuja
    bubbleSort(arr)

    # Imprime el arreglo ya ordenado
    print("Arreglo ordenado:")
    for i in range(len(arr)):
        # Muestra cada elemento en la misma línea
        print("%d" % arr[i], end=" ")
