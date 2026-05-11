# reservas.py

from datetime import datetime
import os

reservas = []
RUTA_RESERVAS = "data/reservas.txt"


def pedir_nombre_cliente():
    while True:
        nombre = input("Introduce el nombre del cliente: ").strip()

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
        else:
            return nombre


def pedir_fecha_reserva():
    while True:
        fecha = input("Introduce la fecha de la reserva (DD/MM/AAAA): ").strip()

        try:
            fecha_convertida = datetime.strptime(fecha, "%d/%m/%Y")

            # Si quieres impedir fechas pasadas, deja esta validación
            if fecha_convertida.date() < datetime.now().date():
                print("Error: no puedes introducir una fecha pasada.")
            else:
                return fecha
        except ValueError:
            print("Error: la fecha debe tener el formato DD/MM/AAAA.")


def pedir_numero_personas():
    while True:
        num_personas = input("Introduce el número de personas: ").strip()

        if not num_personas.isdigit():
            print("Error: debes introducir un número válido.")
        else:
            num_personas = int(num_personas)

            if num_personas <= 0:
                print("Error: el número de personas debe ser mayor que 0.")
            else:
                return num_personas


def mostrar_reservas():
    if len(reservas) == 0:
        print("\nNo hay reservas registradas.\n")
        return

    print("\n--- LISTADO DE RESERVAS ---")
    for i, reserva in enumerate(reservas, start=1):
        print(
            f"{i}. Cliente: {reserva['cliente']} | "
            f"Fecha: {reserva['fecha']} | "
            f"Personas: {reserva['personas']}"
        )
    print()


def gestionar_reserva():
    print("\n--- GESTIÓN DE RESERVAS ---")

    nombre = pedir_nombre_cliente()
    fecha = pedir_fecha_reserva()
    personas = pedir_numero_personas()

    reserva = {
        "cliente": nombre,
        "fecha": fecha,
        "personas": personas
    }

    reservas.append(reserva)
    guardar_reservas()

    print("\nReserva registrada correctamente.")
    print(f"Cliente: {nombre}")
    print(f"Fecha: {fecha}")
    print(f"Número de personas: {personas}\n")
    
def guardar_reservas():
    os.makedirs("data", exist_ok=True)

    with open(RUTA_RESERVAS, "w", encoding="utf-8") as archivo:
        for reserva in reservas:
            archivo.write(
                f"{reserva['cliente']};"
                f"{reserva['fecha']};"
                f"{reserva['personas']}\n"
            )

def cargar_reservas():
    try:
        with open(RUTA_RESERVAS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(";")

                if len(datos) == 3:
                    reserva = {
                        "cliente": datos[0],
                        "fecha": datos[1],
                        "personas": int(datos[2])
                    }

                    reservas.append(reserva)

    except FileNotFoundError:
        os.makedirs("data", exist_ok=True)