class Product:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


class DigitalProduct(Product):
    def __init__(self, name, size, **kwargs):
        super().__init__(name=name, **kwargs)
        self.size = size


class PhysicalProduct(Product):
    def __init__(self, name, weight, **kwargs):
        super().__init__(name=name, **kwargs)
        self.weight = weight


class HybridProduct(DigitalProduct, PhysicalProduct):
    def __init__(self, name, size, weight):
        super().__init__(name=name, size=size, weight=weight)

    def details(self):
        return f"{self.name} includes {self.size} digital files and weighs {self.weight}."
        

hp1 = HybridProduct("Python Mastery", "2GB", "1kg")
print(hp1.details())
