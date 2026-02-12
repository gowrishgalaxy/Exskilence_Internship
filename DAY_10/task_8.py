class Employee:
    def __init__(self, skills):
        self.skills = skills

    def __contains__(self, skill):
        return skill in self.skills


emp = Employee(["Python", "SQL"])

print("Python" in emp)

