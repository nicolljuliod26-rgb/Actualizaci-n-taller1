n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3

if promedio >= 3.0:
    print(f"Promedio: {promedio:.2f} → APRUEBA ✓")
else:
    print(f"Promedio: {promedio:.2f} → REPRUEBA ✗")