cantidad_inicial = int(input("Ingrese la cantidad inicial: "))
vendida = int(input("Ingrese la cantidad vendida: "))
recibida = int(input("Ingrese la cantidad recibida: "))

inventario_final = cantidad_inicial - vendida + recibida

print("El inventario final es:", inventario_final)