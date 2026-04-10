capital = float(input("Ingrese el capital: "))
tasa = float(input("Ingrese la tasa de interés (ejemplo 0.05 para 5%): "))
tiempo = float(input("Ingrese el tiempo en meses: "))

interes = capital * tasa * tiempo
total = capital + interes

print("Interés generado:", interes)
print("Total a pagar:", total)