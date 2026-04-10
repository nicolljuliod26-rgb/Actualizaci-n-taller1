capital = float(input("Capital inicial ($): "))
tasa = float(input("Tasa de interés (% mensual): "))
tiempo = int(input("Tiempo en meses: "))
interes = capital * (tasa / 100) * tiempo
total = capital + interes
print(f"Interés simple: ${interes:,.2f}")
print(f"Total a pagar: ${total:,.2f}")