def crear_pedido(pedidos, clientes, productos):
    try:
        id_pedido = len(pedidos) + 1

        id_cliente = int(input("Ingrese ID del cliente: "))
        if id_cliente not in clientes:
            print("Cliente no existe")
            return pedidos

        id_producto = int(input("Ingrese ID del producto: "))
        if id_producto not in productos:
            print("Producto no existe")
            return pedidos

        cantidad = int(input("Ingrese cantidad: "))
        if cantidad <= 0:
            print("Cantidad inválida")
            return pedidos

        producto = productos[id_producto]
        precio_unitario = producto[2]

        total = precio_unitario * cantidad

        pedidos[id_pedido] = (
            clientes[id_cliente]["nombre"],  # cliente
            producto[1],                     # producto
            cantidad,
            total
        )

        print("Pedido creado correctamente")

    except ValueError:
        print("Error: ingrese valores válidos")

    return pedidos