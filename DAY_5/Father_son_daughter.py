class father:
    def __init__(self, surname, name):
        self.surname=surname
        self.father_name=name

    def display_surname(self):
        print("The surname is: ", self.surname)

    def display_father_name(self):
        print("The father is:", self.father_name) 

class son(father):
    def __init__(self, name, surname, father_name):
        self.name=name
        super().__init__(surname,father_name)

    def display_name(self):
        print("The name of the son is:", self.name)


class daughter(father):
    def __init__(self, name, surname, father_name):
        self.name=name
        super().__init__(surname, father_name)
    def display_name(self):
        print("The name of the daughter is:", self.name)

obj=son("Raj", "S", "Likith")
obj.display_name()
obj.display_father_name()

print()

obj1=daughter("Kumari", "S", "Rajesh")
obj1.display_name()
obj1.display_father_name()