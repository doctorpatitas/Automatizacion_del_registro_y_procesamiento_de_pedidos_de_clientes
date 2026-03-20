from registrar import registrar
from productos import registrar_productos
from order_creation import crear_pedido
from registered_order import mostrar_pedidos
from inventario import calcular_total, generar_reporte

clientes = {}
productos = {}
pedidos = {}

def menu():
    while True:
        print("""
1. Registrar cliente
2. Registrar producto
3. Crear pedido
4. Ver pedidos
5. Calcular ingresos
6. Reporte final
0. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar(clientes)

        elif opcion == "2":
            registrar_productos(productos)

        elif opcion == "3":
            crear_pedido(pedidos, clientes, productos)

        elif opcion == "4":
            mostrar_pedidos(pedidos)

        elif opcion == "5":
            total = calcular_total(pedidos)
            print("Total ingresos:", total)

        elif opcion == "6":
            total_ordenes, total_ingresos, por_cliente, vendidos = generar_reporte(pedidos)

            print("\n==== REPORTE ====")
            print("Total de órdenes:", total_ordenes)
            print("Total de ingresos:", total_ingresos)

            print("\nPedidos por cliente:")
            for cliente, cantidad in por_cliente.items():
                print(f"{cliente}: {cantidad}")

            print("\nProductos vendidos:")
            for producto, cantidad in vendidos.items():
                print(f"{producto}: {cantidad}")

        elif opcion == "0":
            break

        else:
            print("Opción inválida")

menu()