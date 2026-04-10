numeros = [int(input(f"Ingresa el número {i}: ")) for i in range(1, 4)]
print(f"Suma: {sum(numeros)}")
print(f"Promedio: {sum(numeros) / len(numeros):.2f}")