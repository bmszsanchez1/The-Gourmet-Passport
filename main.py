# Main
# main.py

from reservas import gestionar_reserva, mostrar_reservas
from tienda import mostrar_productos, comprar_producto
from menu import mostrar_menu_principal, mostrar_menu, cambiar_pais

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            gestionar_reserva()
        elif opcion == "2":
            mostrar_reservas()
        elif opcion == "3":
            mostrar_productos()
        elif opcion == "4":
            comprar_producto()
        elif opcion == "5":
            mostrar_menu()
        elif opcion == "6":
            cambiar_pais()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")


main()