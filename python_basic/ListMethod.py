# List Methods in Python
List_1 = [1, 2, 3, 4, 5]

# append() -> it adds an element to the end of the list
List_1.append(6)
print(List_1) # [1, 2, 3, 4, 5, 6]

# insert() -> it adds an element at a specific index
List_1.insert(1,7)
print(List_1) # [1, 7, 2, 3, 4, 5, 6]

# remove() -> it removes the first occurrence of the specified element
List_1.remove(7)
print(List_1) # [1, 2, 3, 4, 5, 6]

# pop() -> it removes and returns the last element of the list
last_element = List_1.pop()
print(last_element) # 6
print(List_1) # [1, 2, 3, 4, 5]
List_1.pop(2) # it removes the element at index 2
print(List_1) # [1, 2, 4, 5]

# index() -> it returns the index of the first occurrence of the specified element
List_1.index(4) # 2
print(List_1.index(4)) # 2

List_1.append(4)
List_1.append(2)

# count() -> it returns the number of occurrences of the specified element in the list
print(List_1.count(4)) # 2
print(List_1.count(2)) # 2

# sort() -> it sorts the list in ascending order
List_1.sort()
print(List_1) # [1, 2, 2, 4, 4, 5]

# reverse() -> it reverses the order of the list
List_1.reverse()    
print(List_1) # [5, 4, 4, 2, 2, 1]

# clear() -> it removes all the elements from the list

# enumerate() -> it returns an enumerate object which contains the index and the value of the list

Numbers = [1, 2, 3, 4, 5]
print("Numbers:", Numbers) # [1, 2, 3, 4, 5]
for index_value, value in enumerate(Numbers):
    print(index_value, value)

# length of the list
length = len(Numbers)
print("Length of the list:", length) # 5


# List comprehension -> it is a concise way to create a list
# Syntax -> [expression for item in iterable if condition]
# expression -> it is the value that we want to store in the list
# item -> it is the variable that takes the value of the iterable
# iterable -> it is the collection of items that we want to iterate over
# condition -> it is the optional part that filters the items based on a condition

# I need to store value from 1 to 10 in a list
list_items = [x for x in range(1, 11)]
print(list_items) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_squared = [x**2 for x in list_items]
print(list_squared) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# I need to store only even squared numbers from 1 to 10 in a list
list_even_squared = [x**2 for x in list_items if x%2==0]
print(list_even_squared) # [4, 16, 36, 64, 100]

# function in list comprehension
list_str = ["apple", "banana", "grapes", "orange", "pineapple ", "watermelon"]
list_length = [len(item) for item in list_str]
print(list_length) # [5, 6, 6, 6, 9, 10]