num_ventas = int(input("Número de ventas realizadas en el día: "))
total = 0
for i in range(1, num_ventas + 1):
    valor = float(input(f"Valor de la venta {i} ($): "))
    total += valor

promedio = total / num_ventas
print(f"Total vendido: ${total:,.2f}")
print(f"Promedio por venta: ${promedio:,.2f}")