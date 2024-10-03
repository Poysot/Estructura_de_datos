# Definición de una estructura de datos que contiene otras estructuras de datos
numeros = ((9, 18, (27, 36), 45, "lista"), (54, 63, 72))

# Imprime el cuarto elemento del primer grupo de datos (45)
print(numeros[0][3])

# Imprime el quinto elemento del primer grupo de datos ("lista")
print(numeros[0][4])

# Imprime el primer carácter de la palabra "lista" ('l')
print(numeros[0][4][0])

# Imprime el segundo carácter de la palabra "lista" ('i')
print(numeros[0][4][1])

# Imprime el tercer carácter de la palabra "lista" ('s')
print(numeros[0][4][2])

# Imprime el cuarto carácter de la palabra "lista" ('t')
print(numeros[0][4][3])

# Imprime el quinto carácter de la palabra "lista" ('a')
print(numeros[0][4][4])
