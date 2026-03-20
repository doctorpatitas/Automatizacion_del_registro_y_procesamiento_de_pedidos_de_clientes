#suposicion para que funcione mi parte xd

ordenes = {
    1: ("001", "Laptop", 2, 2000),
    2: ("002", "raton", 3, 150),
    3: ("003", "teclado", 1, 100)
}

def calcular_total(ordenes):
    total = 0
    for orden in ordenes.values():
        cantidad = orden[2]
        precio = orden[3]
        total += cantidad * precio
    return total

def generar_reporte(ordenes):
    total_ordenes = len(ordenes)
    total_ingresos = calcular_total(ordenes)

    ordenes_por_cliente = {}
    productos_vendidos = {}

    for orden in ordenes.values():
        cliente = orden[0]
        producto = orden[1]
        cantidad = orden[2]

        ordenes_por_cliente[cliente] = ordenes_por_cliente.get(cliente, 0) + cantidad
        productos_vendidos[producto] = productos_vendidos.get(producto, 0) + cantidad
    return total_ordenes, total_ingresos, ordenes_por_cliente, productos_vendidos

print("total ingresado:", calcular_total(ordenes))
total_ordenes, total_ingresos, por_cliente, vendidos = generar_reporte(ordenes)

print("\n==== REPORTE ====")
print("Total de órdenes:", total_ordenes)
print("Total de ingresos:", total_ingresos)

print("\nPedidos por cliente:")
for cliente, cantidad in por_cliente.items():
    print(f"Cliente {cliente}: {cantidad} productos")

print("\nProductos vendidos:")
for producto, cantidad in vendidos.items():
    print(f"{producto}: {cantidad} unidades")
