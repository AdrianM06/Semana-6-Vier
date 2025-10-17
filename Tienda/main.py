import funciones as f
from prenda import Prenda


def main():
    prendas = []

    print("Bienvenida a la tienda 'ropa sucia'")

    while True:
        print("Opciones\n")
        print("1. Agregar prenda.")
        print("2. Mostrar todas las prendas.")
        print("3. Buscar prenda por nombre.")
        print("4 Salir.")
    
        opcion = input("\nEscoge una opción:\n--> ")

        if opcion == "1":
            f.agregar_prenda(prendas)
            print("Prenda agregada con éxito\n\n")

        elif opcion == "2":
            f.mostrar_prendas(prendas)

        elif opcion == "3":
            f.buscar_prenda(prendas)

        elif opcion == "4":
            print("Gracias por visitarnos, vuelve pronto!!")
            break


main()
