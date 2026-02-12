class Employee:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Employee {self.name} is working")


emp = Employee("Ravi")
emp()
