class Prenda:
    def __init__(self, nombre, precio, color, marca=""):
        self.nombre = nombre
        self.precio = precio
        self.color = color
        self.marca = marca
        
    def mostrar(self):
        print(f"----{self.nombre}----\nMarca: {self.marca}\nColor: {self.color}\nPrecio: {self.precio}\n")