
# Función para calcular el promedio de tres notas
def calcular_promedio(nota1, nota2, nota3):
    suma = nota1 + nota2 + nota3
    promedio = suma / 3
    return promedio


# Programa principal
if __name__ == "__main__":
    print("=== CALCULO DEL PROMEDIO ===")

    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))

    resultado = calcular_promedio(nota1, nota2, nota3)

    print(f"El promedio de las tres notas es: {resultado:.2f}")
    

