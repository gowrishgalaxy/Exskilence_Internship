class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

dog = Dog("Buddy")
print(dog.speak())