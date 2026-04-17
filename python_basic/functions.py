# Function in python is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as a result.

# you are interviewer welocming cadidate to interview and asking about their name and experience

def greeting(candidatename, experience):
    print(f"Welcome {candidatename} to the interview. You have {experience} years of experience.")

greeting("Hemant", 4)

# create a function which will take number from user and return whether the number is even or odd

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(5))

# Handling error in function

def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(divide(10, 2))
print(divide(10, 0))

# Recursive function -> A recursive function is a function that calls itself in order to solve a problem. 
# It typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"factorial of 5 is {factorial(5)}")  # Output: 120

# base case is when n is 0, the factorial of 0 is defined to be 1.
# recursive case is when n is greater than 0, the factorial of n is defined as n multiplied by the factorial of (n - 1). 
# This breaks down the problem into smaller subproblems until it reaches the base case.


# Function with single parameter/ multiple parameters
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

# Here add has 2 parameters a and b, and it returns the sum of a and b.But if I pass 3 parameters to add function, 
# it will raise an error because it is defined to take only 2 parameters.

# TO handle this error we can use positional arguments and keyword arguments

