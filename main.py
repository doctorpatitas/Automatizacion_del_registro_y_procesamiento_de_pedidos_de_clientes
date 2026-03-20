from registrar import *
from productos import *
from order_creation import crear_pedido
from registered_order import mostrar_pedidos
from inventario import calcular_total, generar_reporte
from login import *


clientes = {}
productos = {}
pedidos = {}

def menu():
    while True:
        print("""
1. Registrar cliente
2. Login cliente
3. Ver pedidos
4. Calcular ingresos
5. Reporte final
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar(clientes)

        elif opcion == "2":
            resultado=login(clientes)
            if resultado=="admin":
                print("modo admin")
                registrarproductos(productos)

            elif resultado=="cliente":
                print("modo cliente")
                crear_pedido(pedidos, clientes, productos)

        
        elif opcion == "3":
            mostrar_pedidos(pedidos)

        elif opcion == "4":
            total = calcular_total(pedidos)
            print("Total ingresos:", total)

        elif opcion == "5":
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

        elif opcion == "6":
            break

        else:
            print("Opción inválida")

menu()