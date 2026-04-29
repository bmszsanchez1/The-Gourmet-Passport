#Tienda

productos = [
    {"nombre": "Salsa picante", "precio": 5, "stock": 10},
    {"nombre": "Té matcha", "precio": 8, "stock": 6},
    {"nombre": "Pasta italiana", "precio": 6, "stock": 12}
]

compras_realizadas = []

def mostrar_productos():
    print("\n-TIENDA GOURMET-")

    for i, producto in enumerate(productos, start=1):
        print(
            f"{i}. {producto['nombre']} | "
            f"Precio: {producto['precio']}€ | "
            f"Stock: {producto['stock']}"
        )

    print()

def comprar_producto():
    mostrar_productos()
    try:
        opcion = int(input("Selecciona el número del producto: "))

        if opcion < 1 or opcion >len(productos):
            print("Error: producto no válido.")
            return
        
        producto = productos[opcion - 1]

        cantidad = int(input("Introduce la cantidad que quieres comprar: "))

        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que 0.")
            return
        
        if cantidad > producto["stock"]:
            print("Error: no hay suficiente stock disponible, disculpa.")
            return
        
        producto["stock"] -= cantidad
        total = producto["precio"] * cantidad
        
        compra = {
            "producto": producto["nombre"],
            "cantidad": cantidad,
            "precio_unitario": producto["precio"],
            "subtotal": total
}

        compras_realizadas.append(compra)

        print("\nCompra realizada con éxito.")
        print(f"Producto: {producto['nombre']}")
        print(f"Cantidad: {cantidad}")
        print(f"Total: {total:.2f}€\n")

    except ValueError:
        print("Error: debes introducir un número válido.")