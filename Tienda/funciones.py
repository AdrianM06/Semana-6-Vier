from prenda import Prenda


def agregar_prenda(prendas):
    nombre = input("Escribe el nombre de la prenda:\n--> ")
    precio = input("Escribe el precio de la prenda:\n--> ")
    color = input("Escribe el color de la prenda:\n--> ")
    marca = input("Escribe el marca de la prenda:\n--> ")

    nueva_prenda = Prenda(nombre, precio, color, marca)
    prendas.append(nueva_prenda)

def mostrar_prendas(prendas):
    if len(prendas) > 0:
        for prenda in prendas:
            prenda.mostrar()
    else:
        print("No hay prendas para mostrar")

def buscar_prenda(prendas):
    nombre = input("nombre de la prenda a buscar:\n--> ")
    prenda_buscada = False
    for prenda in prendas:
        if nombre == prenda.nombre:
            prenda_buscada = prenda

    if not prenda_buscada:
        print("No se encontró la prenda con ese nombre")
    else:
        prenda_buscada.mostrar()

