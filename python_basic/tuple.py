# Tuple _.A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

a = tuple()
print(type(a)) # <class 'tuple'>

tuple_item = (1, 2, 3, 3, 4, 5, "Hello", True, 3.14)

print(tuple_item) # (1, 2, 3, 3, 4, 5, 'Hello', True, 3.14)

print(tuple_item[5]) # 'Hello'

#tuple_item[5] = "World" # TypeError: 'tuple' object does not support item assignment

# len() -> it returns the number of items in the tuple
print(len(tuple_item)) # 9

# TUple methods

# index() -> it returns the index of the first occurrence of the specified element
print(tuple_item.index(3.14)) # 8

# count() -> it returns the number of occurrences of the specified element in the tuple
print(tuple_item.count(3)) # 2


# packing and unpacking of tuples
# packing -> it is the process of assigning values to a tuple