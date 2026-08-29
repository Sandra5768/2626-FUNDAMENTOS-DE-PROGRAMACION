# Crear una matriz de 5 filas por 5 columnas
matriz = [[0 for columna in range(5)] for fila in range(5)]

# Recorrer las filas y columnas mediante bucles anidados
for fila in range(5):
    for columna in range(5):
        # Solicitar al usuario cada valor mediante la consola
        valor = int(input("Ingrese un valor: "))

        # Almacenar el valor en la posición correspondiente
        matriz[fila][columna] = valor

# Recorrer nuevamente la matriz para mostrar sus valores
for fila in range(5):
    for columna in range(5):
        # Mostrar los valores organizados en columnas
        print(matriz[fila][columna], end="\t")

    # Pasar a la siguiente fila
    print()