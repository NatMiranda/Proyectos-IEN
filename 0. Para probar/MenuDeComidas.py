# Menú de comidas

"""
Realizar un programa en Python que simule un menpu de comida rápida. 
El programa debe permitir al usuario:
    - Ver el menú completo.
    - Agregar nuevos elementos al menú.
    - Modificar el precio de un elemento existente 
    - Realizar pedidos.

Cada elemento del menú debe tener:
    - Nombre.
    - Descripción.
    - Precio.

El programa debe ser capaz de calcular el precio total de un pedido y mostrarlo al usuario

Se deberá utilizar: 
    - Una lista para almacenar los elementos del menú.
    - Un diccionario para guardar los pedidos. [La clave será el nombre y el valor la cantidad solicitdada]
"""

import time

class Comida:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

def mostrarMenu(menuPrincipal):
    if not menuPrincipal:
            print("El menú se encuentra vacio.")
    else:
        for comida in menuPrincipal:
            print(f"- Nombre: {comida.nombre}")
            print(f"     Precio: ${comida.precio:.2f}")
            print(f"     Descripción: {comida.descripcion}\n    ")  


def agregarComida():
    nombre = input("Ingrese el nombre de la comida: ")
    precio = float(input("Ingrese el precio de la comida: $"))
    descripcion = input("Ingrese la descripcion de la comida: ")
    print("Aguarde mientras agregamos esta comida al menú...")
    time.sleep(1)

    comida = Comida(nombre, precio, descripcion)
    menuPrincipal.append(comida)
    
    print("...")
    time.sleep(2)
    print("Comida agregada con exito!")

def modificarComida(menu):
    print("Eliga el número de la comida para modificar su precio:")
    if not menu:
        print("El menú está vacío.")
        return menu
    else:
        for i, comida in enumerate(menu):
            print(f"{i + 1}. {comida.nombre}")
        opcion_modif = int(input("---> "))
        if 1 <= opcion_modif <= len(menu):
            indice_modif = opcion_modif - 1
            comida_a_modificar = menu[indice_modif]
            nuevo_precio = float(input(f"Nuevo precio para '{comida_a_modificar.nombre}': $"))
            comida_a_modificar.precio = nuevo_precio
            print(f"Precio de '{comida_a_modificar.nombre}' actualizado a ${comida_a_modificar.precio:.2f}.")
        else:
            print("Opción inválida.")
        return menu    
    
def realizarPedido(menu, pedidos):
    print("¿Que comida quiere agregar?")
    print(mostrarMenu(menu))
    eleccionUsuario = int(input("---> "))

pedidosHechos = dict()

print("_" * 20)
opcion = 1
menuPrincipal = []

print("Bienvenido/a [Usuario/a]")

while opcion != 0:

    print("¿Que le gustaria hacer?")
    print("1. Ver el menú completo.")
    print("2. Agregar nuevos elementos al menú.")
    print("3. Modificar algun elemento del menú.")
    print("4. Realizar un pedido.")
    print("0. Cerrar programa")
    opcion = int(input("---> "))
    
    if opcion == 0:
        print("¡Gracias, vuelvas prontos! Finalizando programa. Aguarde...")
        time.sleep(2)
        print("...")
    elif opcion == 1:
        mostrarMenu(menuPrincipal) 
    elif opcion == 2:
        agregarComida()
    elif opcion == 3:
        menuPrincipal = modificarComida(menuPrincipal)
    elif opcion == 4:
        realizarPedido(menuPrincipal, pedidosHechos)
    else: 
        print("...")
        time.sleep(2)
        print("Opción no disponible o erronea. Volviendo al menú. ")
    print("_" * 20)
    time.sleep(2)











