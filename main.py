# Main
# main.py

from reservas import gestionar_reserva, mostrar_reservas


def mostrar_menu_principal():
    print("= THE GOURMET PASSPORT =")
    print("1. Gestionar reserva")
    print("2. Ver reservas")
    print("3. Salir")


def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            gestionar_reserva()
        elif opcion == "2":
            mostrar_reservas()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")


main()