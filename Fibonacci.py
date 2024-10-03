def salto(n):
    # Retorna 0 si n es igual a 0 (caso base)
    if n == 0:
        return 0
    # Retorna 1 si n es igual a 1 (caso base)
    elif n == 1:
        return 1
    else:
        # Realiza la suma de las dos llamadas anteriores, usando n-1 y n-2
        return salto(n-1) + salto(n-2)

def iniciar():
    try:
        # Solicita un número al usuario, lo convierte en entero
        n = int(input("Introduzca un número para calcular el número de Fibonacci: "))
        if n < 0:
            # Verifica que el número no sea negativo y da un mensaje de advertencia
            print("Error: El número debe ser un entero no negativo.")
        else:
            # Calcula y muestra el resultado del enésimo número de Fibonacci
            print(f"El número de Fibonacci correspondiente a n={n} es {salto(n)}")
    except ValueError:
        # Maneja el error si el usuario ingresa un valor no numérico
        print("Error: Por favor ingrese un número entero válido.")

# Se ejecuta la función iniciar solo si este archivo es ejecutado directamente
if __name__ == "__main__":
    iniciar()
