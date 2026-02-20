"""
Task 1 (Abstraction) – Simple Problem Statement
Animal Sound System

Problem:
Create an Animal system where every animal must make a sound.

Requirements:
1. Create an abstract class Animal.
2. Create an abstract method sound().
3. Create a normal method sleep() common for all animals.
4. Create child classes:
   - Dog → sound() prints Bark
   - Cat → sound() prints Meow
   - Cow → sound() prints Moo
5. Create objects and call sound() and sleep() methods.
"""

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


class Cow(Animal):
    def sound(self):
        print("Moo")


# Create objects
dog = Dog()
cat = Cat()
cow = Cow()

# Call methods
dog.sound()
dog.sleep()

cat.sound()
cat.sleep()

cow.sound()
cow.sleep()
