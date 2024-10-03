# Definición de una estructura de datos que contiene otras estructuras de datos
numeros = ((5, 15, (25, 35), 45, "python"), (60, 75, 90))

# Imprime el cuarto elemento del primer grupo de datos (45)
print(numeros[0][3])

# Imprime el quinto elemento del primer grupo de datos ("python")
print(numeros[0][4])

# Imprime el primer carácter de la palabra "python" ('p')
print(numeros[0][4][0])

# Imprime el segundo carácter de la palabra "python" ('y')
print(numeros[0][4][1])

# Imprime el tercer carácter de la palabra "python" ('t')
print(numeros[0][4][2])

# Imprime el cuarto carácter de la palabra "python" ('h')
print(numeros[0][4][3])

# Imprime el quinto carácter de la palabra "python" ('o')
print(numeros[0][4][4])

# Imprime el sexto carácter de la palabra "python" ('n')
print(numeros[0][4][5])
