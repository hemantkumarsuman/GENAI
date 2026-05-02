# OOP in Python
# OOP stands for Object-Oriented Programming. It is a programming paradigm that uses objects and classes to structure code 
# in a way that is more modular, reusable, and easier to maintain. 
# In Python, you can define classes and create objects to represent real-world entities.
# Define a class -> class ClassName: where ClassName is the name of the class. and 1st letter of the class name should be capital.
class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def introduce(self):
        return f"I am {self.name} and my power is {self.power}"
    
# Create an object of the class -> object_name = ClassName(arguments)

ironman = Avenger("Iron Man", "Genius-level intellect, powered armor suit")
print(ironman.introduce())  # Output: I am Iron Man and my power is Genius-level intellect, powered armor suit

batman = Avenger("Batman", "Peak human physical and mental condition, martial arts skills, high-tech gadgets")
print(batman.introduce())  # Output: I am Batman and my power is    Peak human physical and mental condition, martial arts skills, high-tech gadgets


class Cartoon:
    def __init__(self,name,show):
        self.name = name
        self.show = show
    def introduce(self):
        return f"I am {self.name} and I am from {self.show}"
Mickey_Mouse = Cartoon("Mickey Mouse","Disney")
print(Mickey_Mouse.introduce())  # Output: I am Mickey Mouse and I am from Disney
Pokemon = Cartoon("Charizard","Pokemon")
print(Pokemon.introduce())  # Output: I am Charizard and I am from Pokemon

# Attributes and Methods
# Attributes are variables that belong to an object, while methods are functions that belong to an object.
# In the above example, name and power are attributes of the Avenger class, while introduce is a method of the Avenger class.

# self is a special keyword in Python that refers to the instance of the class.
# It is used to access the attributes and methods of the class within the class itself.
# For example, in the introduce method, self.name and self.power are used to access the name and power attributes of the class.

# Constructor is a special method in Python that is called when an object is created. It is defined using the __init__ method.
# The __init__ method is used to initialize the attributes of the class when an object is created. 
# In the above example, the __init__ method is used to initialize the name and power attributes of the Avenger class 
# when an object is created.
# It get automatically called when an object is created and 
# it takes the arguments that are passed to the class when an object is created.
# Even if we don not define the __init__ method, Python will automatically create a default constructor for the class.
# In the above example, if we do not define the __init__ method, Python will create a default constructor for the Avenger class,
# but we will not be able to initialize the name and power attributes of the class when an object is created.
# Type of constructor:
# 1. Default constructor: A constructor that takes no arguments and initializes the attributes of the class with default values.
# 2. Parameterized constructor: A constructor that takes arguments and initializes the attributes of the 
# class with the values passed as arguments. 
# 3. Copy constructor: A constructor that creates a new object by copying the attributes of an existing object.

# Example of default constructor
class DefaultConstructor:
    def __init__(self):
        self.name = "Default Name"
        self.power = "Default Power"

default_obj = DefaultConstructor()
print(default_obj.name)  # Output: Default Name
print(default_obj.power)  # Output: Default Power

# If we want to change name and power attributes of the default_obj object, we can do it like this:
default_obj.name = "New Name"
default_obj.power = "New Power"
print(default_obj.name)  # Output: New Name
print(default_obj.power)  # Output: New Power

# Example of parameterized constructor
class ParameterizedConstructor:
    def __init__(self, name, power):
        self.name = name
        self.power = power
parameterized_obj = ParameterizedConstructor("Parameterized Name", "Parameterized Power")
print(parameterized_obj.name)  # Output: Parameterized Name
print(parameterized_obj.power)  # Output: Parameterized Power


# TYPES OF METHODS:
# 1. Instance method: A method that takes self as the first parameter and can access the attributes and methods of the class. 
# It is called on an instance of the class.
# 2. Class method: A method that takes cls as the first parameter and can access the class attributes and methods.
# It is called on the class itself.
# 3. Static method: A method that does not take self or cls as the first parameter and cannot access the attributes and methods of the class.
# It is called on the class itself.

# Example of instance method
class InstanceMethod:
    def __init__(self, name):
        self.name = name
    def instance_method(self):
        return f"This is an instance method and my name is {self.name}"
obj1 = InstanceMethod("Hemant")
print(obj1.instance_method())  # Output: This is an instance method and my name is Hemant

# Example of class method
class ClassMethod:
    class_variable = "This is a class variable"
    @classmethod
    def class_method(cls):
        return f"This is a class method and the class variable is {cls.class_variable}"
obj2 = ClassMethod()
print(obj2.class_method())  # Output: This is a class method and the class variable is This is a class variable

# Example of static method
class StaticMethod:
    @staticmethod
    def static_method():
        return "This is a static method"
obj3 = StaticMethod()
print(obj3.static_method())  # Output: This is a static method

# FLow of execution in Python OOP:
# 1. When an object is created, the __init__ method is called to initialize the attributes of the class.
# 2. When a method is called on an object, the method is executed and the self parameter is passed to the method to access the attributes and methods of the class. 
# 3. When a class method is called, the cls parameter is passed to the method to access the class attributes and methods.
# 4. When a static method is called, no parameters are passed to the method as it does not access any attributes or methods of the class.
