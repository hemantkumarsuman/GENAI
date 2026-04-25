# Lambda Function ->  Lambda function is a small anonymous function that can take any number of arguments, 
# but can only have one expression. It is often used for short, simple functions that are not worth defining with a 
# full function definition.

# They can have only one logic or one expression.Can have multiple arguments.

# SYntax -> lambda arguments: expression
# Example 1 -> A lambda function that adds two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example 2 -> A lambda function that squares a number
square = lambda x:x**2
print(square(4))  # Output: 16

print(type(square))  # Output: <class 'function'>

#Example 3 -> A lambda function that checks if a number is even or odd

is_even = lambda x: x%2==0
print(is_even(4))  # Output: True

# MAP -> The map() function applies a given function to each item of an iterable (like a list) and 
# returns a map object (which is an iterator).

# Example 1: Squaring all item of list 
numbers = [1, 2, 3, 4, 5]

# using normal function
def square(numbers):
    emptyList = []
    for item in numbers:
        emptyList.append(item**2)
    return emptyList

squared_numbers = square(numbers)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#using map and lambda function

print(f" Square using map&lambda: {list(map(lambda x:x**2,numbers))}")  # Output: [1, 4, 9, 16, 25]