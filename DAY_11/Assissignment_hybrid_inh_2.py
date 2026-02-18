class Person:
    def __init__(self, name):
        self.name = name


class Faculty(Person):
    def __init__(self, name, subject, department=None):
        super().__init__(name)
        self.subject = subject
        self.department = department

    def teach(self):
        return f"teaches {self.subject}"


class Staff(Person):
    def __init__(self, name, subject=None, department=None):
        super().__init__(name)
        self.subject = subject
        self.department = department

    def work(self):
        return f"works in {self.department} department."


class Administrator(Faculty, Staff):
    def __init__(self, name, subject, department):
        super().__init__(name, subject, department)

    def profile_data(self):
        if self.name:
            return f"{self.name} {self.teach()} and {self.work()}"
        else:
            return f"{self.teach()} and {self.work()}"
