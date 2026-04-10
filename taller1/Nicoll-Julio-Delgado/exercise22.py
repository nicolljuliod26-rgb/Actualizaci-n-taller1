inventario_inicial = int(input("Cantidad inicial en inventario: "))
vendidos = int(input("Cantidad vendida: "))
recibidos = int(input("Cantidad recibida: "))
inventario_final = inventario_inicial - vendidos + recibidos
print(f"Inventario final: {inventario_final} unidades")