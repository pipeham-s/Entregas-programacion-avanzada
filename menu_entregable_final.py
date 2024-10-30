def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Jugar al trivia")
    print("2. Procesar pedidos")
    print("3. Realizar consultas USQL/SQL")

def obtener_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción (1, 2, o 3): "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    mostrar_menu()
    opcion = obtener_opcion()
    print(f"Has seleccionado la opción {opcion}.")