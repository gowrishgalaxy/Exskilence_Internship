class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        return self.emp_id == other.emp_id


e1 = Employee(101, "Ravi")
e2 = Employee(101, "Kiran")

print(e1 == e2)
