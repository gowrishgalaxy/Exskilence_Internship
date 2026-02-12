class EmployeeList:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.employees):
            result = self.employees[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


emps = EmployeeList(["Ravi", "Kiran", "Anu"])

for emp in emps:
    print(emp)
