# Diccionario para guardar estudiantes y sus notas
estudiantes = {}

while True:
    print("\n1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Buscar estudiante")
    print("4. Eliminar estudiante")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar datos al diccionario
    if opcion == "1":
        nombre = input("Nombre: ")
        nota = float(input("Nota: "))
        estudiantes[nombre] = nota
        print("Estudiante agregado.")

    # Mostrar los datos almacenados
    elif opcion == "2":
        for nombre, nota in estudiantes.items():
            print(nombre, "-", nota)

    # Buscar un estudiante
    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        if nombre in estudiantes:
            print("Nota:", estudiantes[nombre])
        else:
            print("Estudiante no encontrado.")

    # Eliminar un estudiante
    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print("Estudiante eliminado.")
        else:
            print("Estudiante no encontrado.")

    # Salir del programa
    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")