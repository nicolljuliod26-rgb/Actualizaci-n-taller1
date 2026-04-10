producto = input("Nombre del producto: ")
precio = float(input("Precio unitario ($): "))
cantidad = int(input("Cantidad comprada: "))
total = precio * cantidad
print(f"Producto: {producto}")
print(f"Total a pagar: ${total:,.2f}")