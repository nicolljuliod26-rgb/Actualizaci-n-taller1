a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print(f"{a} es mayor que {b}.")
elif b > a:
    print(f"{b} es mayor que {a}.")
else:
    print("Los dos números son iguales.")