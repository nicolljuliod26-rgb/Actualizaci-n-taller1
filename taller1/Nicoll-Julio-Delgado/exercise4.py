horas = float(input("Horas trabajadas en la semana: "))
valor_hora = float(input("Valor por hora ($): "))
salario = horas * valor_hora
print(f"Salario semanal: ${salario:,.2f}")