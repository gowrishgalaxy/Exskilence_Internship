"""
Parent Class: Product
Attributes:
product_name
price
Method:
display_product()

Child Class: ElectronicProduct (inherits from Product)
Attributes:
brand
warranty
Method:
display_electronic_product()

Grandchild Class: MobilePhone (inherits from ElectronicProduct)
Attributes:
ram
storage
Method:
display_mobile_details()

Create one object of MobilePhone and display all details.
"""

class Product:
    def __init__(self,product_name,price):
        self.product_name=product_name
        self.price=price

    def display_product(self):
        print("Product :", self.product_name)
        print("Price :", self.price)

class ElectronicProduct(Product):
    def __init__(self,product_name,price ,brand, warranty):
        self.brand=brand
        self.warranty=warranty
        super().__init__(product_name, price)

    def display_electronic_product(self):
        print("Product :", self.product_name)
        print("Price :", self.price)
        print("Brand :", self.brand)
        print("Warranty :", self.warranty)

class MobilePhone(ElectronicProduct):
    def __init__(self,product_name,price ,brand, warranty, ram, storage):
        self.ram = ram
        self.storage = storage
        super().__init__(product_name, price, brand, warranty)

    def display_mobile_details(self):
        print("Product :", self.product_name)
        print("Price :", self.price)
        print("Brand :", self.brand)
        print("Warranty :", self.warranty)
        print("Ram :", self.ram)
        print("Storage :", self.storage)

mobile1= MobilePhone("Samsung Galaxy S26", "15000", "Samsung", "1Year", "16GB", "512GB")

mobile1.display_mobile_details()
