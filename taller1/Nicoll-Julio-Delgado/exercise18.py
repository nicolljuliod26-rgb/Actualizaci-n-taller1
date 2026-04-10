edad = int(input("Ingresa la edad: "))

if edad < 18:
    print("La persona es menor de edad.")
elif edad <= 59:
    print("La persona es adulto.")
else:
    print("La persona es adulto mayor.")