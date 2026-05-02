# Exception Handling -> Used to handle errors and exceptions in Python code.
# Try and Except Block -> Used to catch and handle exceptions.

# without try/except block
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = num1 / num2
# print("Result: ", result)

# If num2 is 0, it will raise a ZeroDivisionError and the program will crash. To handle this, we can use a try/except block.

# with try/except block
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result: ", result)       
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Different types of exceptions:
# 1. ZeroDivisionError -> Raised when division by zero is attempted.
# 2. ValueError -> Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.
# 3. TypeError -> Raised when an operation or function is applied to an object of
#    inappropriate type.
# 4. FileNotFoundError -> Raised when a file or directory is requested but doesn't exist.
# 5. KeyError -> Raised when a dictionary key is not found.

