def factorial(n):
    # Verifica si n es 0 o 1, en cuyo caso devuelve 1 directamente
    if (n <= 1):
        return 1
    else:
        # Calcula el factorial del número anterior (n-1)
        subSolution = factorial(n - 1)
        # Multiplica el resultado previo por n para obtener la solución
        solution = subSolution * n
        # Devuelve el valor calculado
        return solution

try:
    # Pide un número al usuario y lo convierte a un entero
    n = int(input("Ingrese un número para calcular su factorial: "))
    # Muestra el resultado del factorial calculado en la pantalla
    print(f"El factorial de {n} es {factorial(n)}")
except ValueError:
    # Avisa al usuario si el valor ingresado no es un número entero
    print("Error: Ingrese un número entero válido.")
