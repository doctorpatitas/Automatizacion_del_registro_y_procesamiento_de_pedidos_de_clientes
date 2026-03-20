productos = {}

def registrar_productos(productos):

    while True:
        try:
            product_id = int(input("Ingrese ID del producto: "))
        except ValueError:
            print("Ingrese un número válido")
            continue

        if product_id in productos:
            print("Ese ID ya existe")
            continue

        nombre = input("Ingrese nombre del producto: ").lower().strip()

        try:
            precio = float(input("Ingrese precio: "))
            cantidad=int(input("ingrese la cantidada: "))
        except ValueError:
            print("Precio inválido")
            continue

       
        producto = (product_id, nombre, precio, cantidad)

        
        productos[product_id] = producto

        otro = input("¿Registrar otro producto? (si/no): ").lower()
        if otro == "no":
            break

    return productos

