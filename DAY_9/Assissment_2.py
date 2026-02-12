"""
Task 2 (Class Variable + Classmethod + Staticmethod) – Simple Problem Statement
Student College System

Problem:
Create a student system where the college name is the same for all students.

Requirements:
1. Create a class Student.
2. Create a class variable college_name = "ABC College".
3. Constructor takes name and roll_no.
4. Create a classmethod change_college(new_name) to update college name.
5. Create a staticmethod is_pass(marks) to check pass or fail.
6. Create an instance method display() to print student details.
7. Create 2 students, display details.
8. Change college name using classmethod.
9. Display details again.
10. Use staticmethod to check pass or fail.
"""


class Student:
    # Class variable
    college_name = "ABC College"

    # Constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    # Instance method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
        print()

    # Class method
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name

    # Static method
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"


# Create student objects
student1 = Student("Sita", 101)
student2 = Student("Krishna", 102)

# Display student details
student1.display()
student2.display()

# Change college name using classmethod
Student.change_college("XYZ Engineering College")

# Display details again
student1.display()
student2.display()

# Use staticmethod
print("Student1 Result:", Student.is_pass(78))
print("Student2 Result:", Student.is_pass(32))
