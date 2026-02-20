"""
Task-1: Polymorphism – Payment System

Problem Statement:
Create a program for a Payment System using method overriding.

Requirements:
1. Create a parent class Payment with method pay().
2. Create a child class GooglePay that inherits Payment and overrides pay().
3. Create a child class PhonePe that inherits Payment and overrides pay().
4. Create a child class CreditCard that inherits Payment and overrides pay().
5. Create one object for each class and call the pay() method.
"""

class Payment:
    def pay(self):
        print("Processing payment using a generic payment method")


class GooglePay(Payment):
    def pay(self):
        print("Payment completed using Google Pay")


class PhonePe(Payment):
    def pay(self):
        print("Payment completed using PhonePe")


class CreditCard(Payment):
    def pay(self):
        print("Payment completed using Credit Card")


# Create objects
payment = Payment()
gpay = GooglePay()
phonepe = PhonePe()
card = CreditCard()

# Call pay() method
payment.pay()
gpay.pay()
phonepe.pay()
card.pay()
