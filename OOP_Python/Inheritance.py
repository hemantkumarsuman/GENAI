# Inheritance in Python -> Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a new class (called a child or subclass) to inherit attributes and behaviors (methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes. 
# In simple terms, inheritance allows you to create a new class that is a modified version of an existing class, without having to rewrite the entire code. 
# Example of Inheritance in Python
# Parent class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"
# Child class (subclass) that inherits from Animal
class Dog(Animal):
    def speak(self):
        return "Woof!"
# Child class (subclass) that inherits from Animal
class Cat(Animal):
    def speak(self):
        return "Meow!"
# Creating instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.name)  # Output: Buddy
print(dog.speak())  # Output: Woof!
print(cat.name)  # Output: Whiskers
print(cat.speak())  # Output: Meow!

# What really happens is that the Dog and Cat classes inherit the __init__ method from the Animal class, 
# allowing them to initialize the name attribute without having to redefine the __init__ method in each subclass. 
# They also override the speak method to provide specific behavior for dogs and cats.

# TYPES OF INHERITANCE IN PYTHON
# 1. Single Inheritance: A child class inherits from a single parent class.
class AvengerParent:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    def introduce(self):
        return f"I am {self.name} and my power is {self.power}."
class AvengerChild(AvengerParent):
    def __init__(self,name, power,weapon):
        super().__init__(name, power)  # Call the parent class's __init__ method
        self.weapon = weapon
    def weapon_info(self):
        return f"My weapon is {self.weapon}."

obj1 = AvengerChild("Flash", "Super Speed", "Lightning Bolt")
print(obj1.introduce())
print(obj1.weapon_info())
print(obj1.name)
print(obj1.power)
print(obj1.weapon)

# 2. Multilevel Inheritance: The method and properties of grandparent class is inherited by parent class and 
#                          then property of parent class is inherited by child class.

class grandParent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def grandparent_method(self):
        return f"I am the grandparent, my name is {self.name} and I am {self.age} years old."
class parent(grandParent):
    def __init__(self, name, age, occupation):
        super().__init__(name, age)  # Call the grandparent class's __init__ method
        self.occupation = occupation
    def parent_method(self):
        return f"I am the parent, my name is {self.name}, I am {self.age} years old and I work as a {self.occupation}."
class child(parent):
    def __init__(self, name, age, occupation, school):
        super().__init__(name, age, occupation)  # Call the parent class's __init__ method
        self.school = school
    def child_method(self):
        return f"I am the child, my name is {self.name}, I am {self.age} years old, I work as a {self.occupation} and I go to {self.school}."
obj2 = child("Alice", 10, "Student", "Greenwood High")
print(obj2.grandparent_method())
print(obj2.parent_method())
print(obj2.child_method())  


# 3. Multiple Inheritance: A child class inherits more than one parent class. 
# The child class can access attributes and methods from all parent classes.

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
    def bank_info(self):
        return f"I am a customer of {self.bank_name}."
class CreditCard:
    def __init__(self, card_type):
        self.card_type = card_type
    def card_info(self):
        return f"I have a {self.card_type} credit card."
class Customer(Bank, CreditCard):
    def __init__(self, bank_name, card_type, customer_name):
        Bank.__init__(self, bank_name)  # Initialize Bank class
        CreditCard.__init__(self, card_type)  # Initialize CreditCard class
        self.customer_name = customer_name
    def customer_info(self):
        return f"My name is {self.customer_name}, I am a customer of {self.bank_name} and I have a {self.card_type} credit card."
customer = Customer("ABC Bank", "Visa", "John Doe")
print(customer.bank_info())  # Output: I am a customer of ABC Bank.
print(customer.card_info())  # Output: I have a Visa credit card.
print(customer.customer_info())  # Output: My name is John Doe, I am a customer of ABC Bank and I have a Visa credit card.

# Note: In multiple inheritance, if there are methods with the same name in both parent classes, the method resolution order (MRO)
# determines which method is called. The MRO follows a specific order (depth-first, left-to-right) to resolve method calls.
# For example, if both Bank and CreditCard had a method called info(), the Customer class would call the info() method from 
# the Bank class first, because Bank is listed before CreditCard in the class definition.
