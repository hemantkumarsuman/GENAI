# Set -> A collection of unique elements stored in curly braces {}. Sets are unordered and do not allow duplicate values.
# Syntax: set_name = {element1, element2, ...}
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))  # Output: <class 'set'>

# Method in Set
# 1) add() -> Adds an element to the set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# 2) remove() -> Removes an element from the set. Raises KeyError if the element is not found.
my_set.remove(3)
my_set.remove(10)  # This will raise KeyError since 10 is not in the set

