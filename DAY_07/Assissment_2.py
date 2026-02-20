"""
Task-2: Abstraction – Vehicle System

Problem Statement:
Create a program for a Vehicle System using Abstraction.

Requirements:
1. Create an abstract class Vehicle.
2. Create an abstract method start_engine().
3. Create a child class Car and implement start_engine().
4. Create a child class Bike and implement start_engine().
5. Create a child class Bus and implement start_engine().
6. Create objects of each child class and call start_engine().
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")


class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started")


# Create objects
car = Car()
bike = Bike()
bus = Bus()

# Call methods
car.start_engine()
bike.start_engine()
bus.start_engine()
