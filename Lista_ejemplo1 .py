# Definición de una estructura de datos que contiene otras estructuras de datos
numeros = ((10, 20, (30, 50), 80, "mundo"), (25, 55, 85))

# Imprime el cuarto elemento del primer grupo de datos (80)
print(numeros[0][3])

# Imprime el quinto elemento del primer grupo de datos ("mundo")
print(numeros[0][4])

# Imprime el primer carácter de la palabra "mundo" ('m')
print(numeros[0][4][0])

# Imprime el segundo carácter de la palabra "mundo" ('u')
print(numeros[0][4][1])

# Imprime el tercer carácter de la palabra "mundo" ('n')
print(numeros[0][4][2])

# Imprime el cuarto carácter de la palabra "mundo" ('d')
print(numeros[0][4][3])

# Imprime el quinto carácter de la palabra "mundo" ('o')
print(numeros[0][4][4])
