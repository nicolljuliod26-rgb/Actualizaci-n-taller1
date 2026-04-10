ventas = float(input("Valor total de ventas ($): "))
comision = ventas * 0.05
total = ventas + comision
print(f"Comisión (5%): ${comision:,.2f}")
print(f"Total a recibir: ${total:,.2f}")