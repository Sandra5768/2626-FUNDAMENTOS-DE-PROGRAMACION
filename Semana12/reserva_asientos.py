# Crear una matriz de 3 filas y 4 columnas, con todos sus valores inicializados en 0
asientos = [[0 for columna in range(4)] for fila in range(3)]

# Solicitar al usuario la fila y la columna del asiento que desea reservar
fila = int(input("Ingrese fila (0 a 2): "))
columna = int(input("Ingrese columna (0 a 3): "))

# Asignar el valor 1 al asiento seleccionado para indicar que está reservado
asientos[fila][columna] = 1

# Mostrar el estado completo de la sala de cine
print("Estado de la sala:")

# Recorrer las filas y columnas mediante dos bucles anidados
for fila in range(3):
    for columna in range(4):
        # Mostrar los valores de cada fila sin realizar un salto de línea
        print(asientos[fila][columna], end=" ")
    # Pasar a la siguiente línea después de completar cada fila
    print()