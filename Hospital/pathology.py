
class Pathology:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def show_attr(self):
        return f"----{self.id}----\nNombre: {self.name} - Precio: {self.price}\n"
    