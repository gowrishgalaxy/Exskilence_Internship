class EmployeeFile:
    def __enter__(self):
        print("Opening employee file")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing employee file")


with EmployeeFile() as file:
    print("Working with employee data")
