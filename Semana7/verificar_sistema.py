def main():
    # Indica si el sistema está activo
    sistema_activo = True

    # Indica si el usuario tiene permiso
    tiene_permiso = True

    # Se verifica primero si el sistema está activo
    if sistema_activo:

        # Si el sistema está activo, se comprueba el permiso del usuario
        if tiene_permiso:
            print("La acción puede ejecutarse.")
        else:
            print("El usuario no tiene permiso para ejecutar la acción.")

    # Si el sistema no está activo, se muestra este mensaje
    else:
        print("El sistema se encuentra inactivo.")


# Llamada a la función principal del programa
main()