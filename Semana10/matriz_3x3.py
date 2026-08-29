def main():
    matriz = [
        [8, 3, 5],
        [2, 9, 1],
        [6, 4, 7]
    ]

    for i in range(3):
        for j in range(3):
            print(matriz[i][j], end=" ")
        print()


if __name__ == "__main__":
    main()