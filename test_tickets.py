from tickets import calcular_total


def test_calcular_total():
    compras_prueba = [
        {"subtotal": 10},
        {"subtotal": 15},
        {"subtotal": 5}
    ]

    total = calcular_total(compras_prueba)

    assert total == 30


test_calcular_total()
print("Test de tickets completado correctamente.")