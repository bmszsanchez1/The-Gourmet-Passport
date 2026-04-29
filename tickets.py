#Tickets

from datetime import datetime
from tienda import compras_realizadas


def calcular_total():
    total_final = 0

    for compra in compras_realizadas:
        total_final += compra["subtotal"]

    return total_final


def mostrar_ticket():
    if len(compras_realizadas) == 0:
        print("\nNo hay productos comprados. No se puede generar un ticket vacío.\n")
        return

    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
    total_final = calcular_total()

    print("\n================================")
    print("       THE GOURMET PASSPORT")
    print("================================")
    print(f"Fecha: {fecha_actual}")
    print("=" * 32)
    print("Productos comprados:")

    for compra in compras_realizadas:
        print(
            f"- {compra['producto']} | "
            f"Cantidad: {compra['cantidad']} | "
            f"Precio: {compra['precio_unitario']}€ | "
            f"Subtotal: {compra['subtotal']:.2f}€"
        )

    print("--------------------------------")
    print(f"TOTAL FINAL: {total_final:.2f}€")
    print("================================\n")
    
    compras_realizadas.clear()
    print("Gracias por su compra.\n")