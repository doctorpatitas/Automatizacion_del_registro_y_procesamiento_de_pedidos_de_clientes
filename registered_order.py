def mostrar_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados")
        return pedidos

    print("\n=== PEDIDOS REGISTRADOS ===")

    for id_pedido, datos in pedidos.items():
        cliente = datos[0]
        producto = datos[1]
        cantidad = datos[2]
        total = datos[3]

        print(f"""
Pedido ID: {id_pedido}
Cliente: {cliente}
Producto: {producto}
Cantidad: {cantidad}
Total: {total}
""")

    return pedidos