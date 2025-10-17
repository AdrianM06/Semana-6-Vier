
class Animal:
    def __init__(self, color):
        self.color = color

    def hacer_ruido(self):
        print("Ruido de animal")

    def mostrar(self):
        print(f"Color: {self.color}")

class Gato(Animal):
    def __init__(self, color, tamaño, nombre=""):
        super().__init__(color)
        self.tamaño = tamaño

    def hacer_ruido(self):
        print("miau")

    def mostrar(self):
        print(f"Gato\nColor: {self.color}, Tamaño: {self.tamaño}")

un_gato = Gato("naranja", "medio metro")

un_gato.mostrar()

print("Adoptar al gato: ")
un_gato.nombre = input("Nombre del gato:\n--> ")

print(f"Felicidades!! Has adoptado al gato y le pusiste: {un_gato.nombre}")
