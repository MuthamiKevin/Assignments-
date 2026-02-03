
"""
1. Class and Object Basics
Define a class named Student with the following attributes:
name
age
grade
Create a method display_info() that prints the student's details.
Create three student objects and call the method for each to display their details.
"""
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


student1 = Student("Kevin", 21, "A")
student2 = Student("Aisha", 20, "B")
student3 = Student("Brian", 22, "A-")

student1.display_info()
student2.display_info()
student3.display_info()

"""2. Instance vs Class Methods
Define a class named BankAccount with:
account_number
balance
Add methods:
deposit(amount)
withdraw(amount)
display_balance()
Add a class variable to store the bank name and a class method to display the bank name.
Create two account objects and perform deposits and withdrawals."""
class BankAccount:
    bank_name = "Global Bank"

    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    @classmethod
    def display_bank_name(cls):
        print(f"Bank Name: {cls.bank_name}")


acc1 = BankAccount("001", 1000)
acc2 = BankAccount("002", 500)

acc1.deposit(300)
acc1.withdraw(200)
acc1.display_balance()

acc2.withdraw(700)
acc2.display_balance()

BankAccount.display_bank_name()




"""3. Encapsulation
Create a class Car with:
Private attributes: __make, __model, __year, __speed
Methods to:
Get and set make, model, and year.
Increase and decrease speed.
Display all car details.
Create a Car object, update its attributes, and demonstrate encapsulation."""
class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__speed = 0

    # getters
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # setters
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def accelerate(self, value):
        self.__speed += value

    def brake(self, value):
        self.__speed = max(0, self.__speed - value)

    def display_details(self):
        print(self.__make, self.__model, self.__year, "Speed:", self.__speed)
        
        
car = Car("Toyota", "Corolla", 2020)
car.accelerate(60)
car.brake(20)
car.set_year(2022)
car.display_details()



"""
4. Methods with Objects as Arguments
Create a class Circle with:
Attributes: radius
Method area() and circumference().
Create a class Cylinder that takes a Circle object and height.
Method volume() to compute the volume using the circle's area.
Demonstrate by creating a Circle object and passing it to the Cylinder object.
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

class Cylinder:
    def __init__(self, circle, height):
        self.circle = circle
        self.height = height

    def volume(self):
        return self.circle.area() * self.height

circle = Circle(7)
cylinder = Cylinder(circle, 10)

print("Cylinder Volume:", cylinder.volume())


"""
5. Object Relationships (Aggregation)
Create a class Author with:
Attributes: name, nationality
Method to display author info.
Create a class Book with:
Attributes: title, price, and author (Author object).
Method to display book details including author info.
Create one author and multiple books related to that author."""

class Author:
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    def display_info(self):
        print(f"Author: {self.name}, Nationality: {self.nationality}")


class Book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def display_details(self):
        print(f"Title: {self.title}, Price: {self.price}")
        self.author.display_info()
        
author = Author("Chinua Achebe", "Nigerian")

book1 = Book("Things Fall Apart", 1200, author)
book2 = Book("No Longer at Ease", 1000, author)

book1.display_details()
book2.display_details()

"""
6. Assignment Challenge (Optional)
Create a class Rectangle with:
Attributes: length and width
Method area() and perimeter().
Write a method that takes another rectangle object as an argument and compares their areas.
Create multiple rectangles and compare them."""

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def compare_area(self, other):
        if self.area() > other.area():
            return "First rectangle is larger"
        elif self.area() < other.area():
            return "Second rectangle is larger"
        else:
            return "Both rectangles have equal area"
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 6)

print("Rect1 Area:", rect1.area())
print("Rect2 Area:", rect2.area())
print(rect1.compare_area(rect2))
