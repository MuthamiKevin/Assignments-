
"""
1. Class and Object Basics
Define a class named Student with the following attributes:
name
age
grade
Create a method display_info() that prints the student's details.
Create three student objects and call the method for each to display their details.
"""
# Define the Student class to represent a student with name, age, and grade
class Student:
    # Constructor to initialize Student object with name, age, and grade
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student's information
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


# Create three student objects
student1 = Student("Kevin", 21, "A")
student2 = Student("Aisha", 20, "B")
student3 = Student("Brian", 22, "A-")

# Display information for each student
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
# Define the BankAccount class to manage bank account operations
class BankAccount:
    # Class variable shared by all instances
    bank_name = "Global Bank"

    # Constructor to initialize account number and balance
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    # Instance method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

    # Instance method to withdraw money from the account
    def withdraw(self, amount):
        # Check if sufficient funds are available
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.balance}")
        else:
            print("Insufficient funds")

    # Instance method to display current account balance
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    # Class method to display the bank name (shared across all instances)
    @classmethod
    def display_bank_name(cls):
        print(f"Bank Name: {cls.bank_name}")


# Create two bank account objects
acc1 = BankAccount("001", 1000)
acc2 = BankAccount("002", 500)

# Perform deposit and withdrawal operations on account 1
acc1.deposit(300)
acc1.withdraw(200)
acc1.display_balance()

# Perform withdrawal operation on account 2
acc2.withdraw(700)
acc2.display_balance()

# Display bank name using class method
BankAccount.display_bank_name()




"""3. Encapsulation
Create a class Car with:
Private attributes: __make, __model, __year, __speed
Methods to:
Get and set make, model, and year.
Increase and decrease speed.
Display all car details.
Create a Car object, update its attributes, and demonstrate encapsulation."""
# Define the Car class with private attributes to demonstrate encapsulation
class Car:
    # Constructor to initialize private Car attributes
    def __init__(self, make, model, year):
        self.__make = make          # Private attribute: car make
        self.__model = model        # Private attribute: car model
        self.__year = year          # Private attribute: car year
        self.__speed = 0            # Private attribute: current speed

    # Getter methods to access private attributes
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    # Setter methods to modify private attributes
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    # Method to increase the car's speed
    def accelerate(self, value):
        self.__speed += value

    # Method to decrease the car's speed (ensuring it doesn't go below 0)
    def brake(self, value):
        self.__speed = max(0, self.__speed - value)

    # Method to display all car details
    def display_details(self):
        print(self.__make, self.__model, self.__year, "Speed:", self.__speed)
        
# Create a Car object
car = Car("Toyota", "Corolla", 2020)
# Test car operations
car.accelerate(60)   # Increase speed
car.brake(20)        # Decrease speed
car.set_year(2022)   # Update year using setter
car.display_details()  # Display car information



"""
4. Methods with Objects as Arguments
Create a class Circle with:
Attributes: radius
Method area() and circumference().
Create a class Cylinder that takes a Circle object and height.
Method volume() to compute the volume using the circle's area.
Demonstrate by creating a Circle object and passing it to the Cylinder object.
"""
# Import math module for mathematical constants and functions
import math

# Define the Circle class
class Circle:
    # Constructor to initialize circle with radius
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate the area of the circle
    def area(self):
        return math.pi * self.radius ** 2

    # Method to calculate the circumference of the circle
    def circumference(self):
        return 2 * math.pi * self.radius

# Define the Cylinder class that uses a Circle object
class Cylinder:
    # Constructor that takes a Circle object and height as arguments
    def __init__(self, circle, height):
        self.circle = circle  # Store the Circle object
        self.height = height

    # Method to calculate volume using the circle's area
    def volume(self):
        return self.circle.area() * self.height

# Create a Circle object with radius 7
circle = Circle(7)
# Create a Cylinder object using the Circle object and height 10
cylinder = Cylinder(circle, 10)

# Calculate and display the cylinder volume
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

# Define the Author class
class Author:
    # Constructor to initialize author with name and nationality
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality

    # Method to display author information
    def display_info(self):
        print(f"Author: {self.name}, Nationality: {self.nationality}")


# Define the Book class that has an Author object (aggregation)
class Book:
    # Constructor to initialize book with title, price, and Author object
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author  # Author object reference

    # Method to display book details and author information
    def display_details(self):
        print(f"Title: {self.title}, Price: {self.price}")
        self.author.display_info()  # Call author's display method
        
# Create one Author object
author = Author("Chinua Achebe", "Nigerian")

# Create multiple Book objects with the same author
book1 = Book("Things Fall Apart", 1200, author)
book2 = Book("No Longer at Ease", 1000, author)

# Display details for each book (includes author info)
book1.display_details()
book2.display_details()

"""
6. Assignment Challenge (Optional)
Create a class Rectangle with:
Attributes: length and width
Method area() and perimeter().
Write a method that takes another rectangle object as an argument and compares their areas.
Create multiple rectangles and compare them."""

# Define the Rectangle class
class Rectangle:
    # Constructor to initialize rectangle with length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to calculate the area of the rectangle
    def area(self):
        return self.length * self.width

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.length + self.width)

    # Method to compare the area of this rectangle with another Rectangle object
    def compare_area(self, other):
        if self.area() > other.area():
            return "First rectangle is larger"
        elif self.area() < other.area():
            return "Second rectangle is larger"
        else:
            return "Both rectangles have equal area"

# Create two Rectangle objects with different dimensions
rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 6)

# Display areas of both rectangles
print("Rect1 Area:", rect1.area())
print("Rect2 Area:", rect2.area())
# Compare the areas of both rectangles
print(rect1.compare_area(rect2))
