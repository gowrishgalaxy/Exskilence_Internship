class Employee:
    def __del__(self):
        print("Employee object deleted")


emp = Employee()
del emp
