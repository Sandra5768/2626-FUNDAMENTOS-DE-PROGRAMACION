# Programa para calcular el total de una compra

def calcular_total(precio, cantidad):
    total = precio * cantidad
    return total


if __name__ == "__main__":
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad de productos: "))

    total = calcular_total(precio, cantidad)

    print(f"El total de la compra es: ${total:.2f}")