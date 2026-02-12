class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employee({self.emp_id}, '{self.name}', {self.salary})"


emp = Employee(101, "Ravi", 50000)

print(str(emp))     # calls __str__
print(repr(emp))    # calls __repr__
