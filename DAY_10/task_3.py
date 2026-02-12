class Employee:
    def __new__(cls, *args, **kwargs):
        print("Creating object using __new__")
        return super().__new__(cls)

    def __init__(self, name):
        print("Initializing object using __init__")
        self.name = name


emp = Employee("Ravi")

