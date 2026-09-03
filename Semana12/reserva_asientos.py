# Crear una matriz de 3 filas por 4 columnas inicializada en 0
asientos = [[0 for columna in range(4)] for fila in range(3)]

# Pedir al usuario la fila y la columna del asiento
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Marcar el asiento como reservado
asientos[fila][columna] = 1

# Mostrar el estado de la sala
print("Estado de la sala:")

# Recorrer la matriz con dos bucles anidados
for fila in range(3):
    for columna in range(4):
        print(asientos[fila][columna], end=" ")
    print()