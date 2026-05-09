# Testing Manual - The Gourmet Passport

## Objetivo
Comprobar que el programa funciona correctamente, que todas las opciones del menú responden y que se controlan entradas incorrectas.

## Pruebas realizadas

| ID | Módulo | Prueba | Resultado esperado | Resultado |
|---|---|---|---|---|
| T01 | Menú principal | Introducir opción válida | Accede al módulo correcto | Superado |
| T02 | Menú principal | Introducir opción inválida | Muestra mensaje de error | Superado |
| T03 | Reservas | Crear reserva correcta | Reserva registrada | Superado |
| T04 | Reservas | Nombre vacío | Muestra error | Superado |
| T05 | Reservas | Fecha incorrecta | Muestra error de formato | Superado |
| T06 | Reservas | Número de personas inválido | Muestra error | Superado |
| T07 | Reservas | Ver reservas | Muestra reservas guardadas | Superado |
| T08 | Tienda | Ver productos | Muestra productos con precio y stock | Superado |
| T09 | Tienda | Comprar producto correcto | Reduce stock y registra compra | Superado |
| T10 | Tienda | Stock insuficiente | Muestra error | Superado |
| T11 | Menú dinámico | Seleccionar país válido | Muestra platos del país | Superado |
| T12 | Menú dinámico | Seleccionar país inválido | Muestra error | Superado |
| T13 | Menú dinámico | Cambiar país del mes | Actualiza menú correctamente | Superado |
| T14 | Tickets | Generar ticket sin compras | No genera ticket vacío | Superado |
| T15 | Tickets | Generar ticket con compras | Muestra productos, subtotales y total | Superado |
| T16 | Archivos | Crear reserva | Guarda en data/reservas.txt | Superado |
| T17 | Archivos | Generar ticket | Guarda venta en data/ventas.txt | Superado |

## Conclusión
Tras realizar las pruebas manuales, el programa funciona correctamente. Se han comprobado los módulos principales: reservas, tienda, menú dinámico, tickets y guardado en archivos. También se han probado entradas incorrectas para verificar que el programa muestra errores adecuados y no se detiene inesperadamente.