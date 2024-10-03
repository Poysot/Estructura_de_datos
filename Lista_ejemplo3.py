# Definición de una estructura de datos que contiene otras estructuras de datos
numeros = ((7, 14, (21, 28), 35, "codigo"), (42, 49, 56))

# Imprime el cuarto elemento del primer grupo de datos (35)
print(numeros[0][3])

# Imprime el quinto elemento del primer grupo de datos ("codigo")
print(numeros[0][4])

# Imprime el primer carácter de la palabra "codigo" ('c')
print(numeros[0][4][0])

# Imprime el segundo carácter de la palabra "codigo" ('o')
print(numeros[0][4][1])

# Imprime el tercer carácter de la palabra "codigo" ('d')
print(numeros[0][4][2])

# Imprime el cuarto carácter de la palabra "codigo" ('i')
print(numeros[0][4][3])

# Imprime el quinto carácter de la palabra "codigo" ('g')
print(numeros[0][4][4])

# Imprime el sexto carácter de la palabra "codigo" ('o')
print(numeros[0][4][5])
