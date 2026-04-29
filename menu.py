# menu.py
pais_del_mes = None

menus_por_pais = {
    "mexico": [
        {"plato": "Tacos al pastor", "precio": 9},
        {"plato": "Guacamole con nachos", "precio": 6},
        {"plato": "Churros con chocolate", "precio": 5}
    ],
    "japon": [
        {"plato": "Sushi variado", "precio": 14},
        {"plato": "Ramen", "precio": 11},
        {"plato": "Mochis", "precio": 5}
    ],
    "italia": [
        {"plato": "Pizza margarita", "precio": 10},
        {"plato": "Pasta carbonara", "precio": 12},
        {"plato": "Tiramisú", "precio": 6}
    ],
    "india": [
        {"plato": "Pollo tikka masala", "precio": 13},
        {"plato": "Arroz basmati", "precio": 5},
        {"plato": "Naan", "precio": 4}
    ]
}

def cambiar_pais():
    global pais_del_mes
    pais_del_mes = seleccionar_pais_del_mes()
    print(f"\nPaís del mes cambiado a: {pais_del_mes.capitalize()}\n")

def mostrar_menu_principal():
    print("= THE GOURMET PASSPORT =")
    print("1. Gestionar reserva")
    print("2. Ver reservas")
    print("3. Ver productos de tienda")
    print("4. Comprar producto")
    print("5. Ver menú dinámico")
    print("6. Cambiar país del mes")
    print("7. Mostrar ticket")
    print("8. Salir")


def mostrar_paises_disponibles():
    print("\nPaíses disponibles:")
    for pais in menus_por_pais:
        print(f"- {pais.capitalize()}")


def seleccionar_pais_del_mes():
    while True:
        mostrar_paises_disponibles()
        pais = input("Introduce el país del mes: ").strip().lower()

        if pais in menus_por_pais:
            return pais
        else:
            print("Error: país no disponible. Inténtalo de nuevo.")


def mostrar_menu():
    global pais_del_mes

    print("\n--- MENÚ DINÁMICO DEL MES ---")

    # Si no hay país seleccionado, lo pedimos una vez
    if pais_del_mes is None:
        pais_del_mes = seleccionar_pais_del_mes()

    platos = menus_por_pais[pais_del_mes]

    print(f"\nMenú temático de {pais_del_mes.capitalize()}:")

    for i, plato in enumerate(platos, start=1):
        print(
            f"{i}. {plato['plato']} | "
            f"Precio: {plato['precio']}€"
        )

    print()