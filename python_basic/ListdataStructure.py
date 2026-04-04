# Data Structures in Python
# List, Tuple, Set, Dictionary

# Different type of data structures differ on the basis of how they store data.


print("Data Structures in Python")

#LIST

lists = ["mango", "banana", "grapes", "orange", "pineapple ", "watermelon"];

print(lists[5]) # watermelon
print(lists[0]) # mango

print(lists[-1]) # watermelon
print(lists[-2]) # pineapple

# To access all stored value we can use :

print(lists[:]) # ['mango', 'banana', 'grapes', 'orange', 'pineapple ', 'watermelon']

# List slicing -> can help us with retirving a portion of the list
# first index is inclusive and second index is exclusive
print(lists[1:4]) # ['banana', 'grapes', 'orange']
print(lists[2:]) # ['grapes', 'orange', 'pineapple ', 'watermelon']
print(lists[:3]) # ['mango', 'banana', 'grapes']

# list reverse
# How it works -> it starts from the end of the list and moves towards the beginning of the list
print(lists[::-1]) # ['watermelon', 'pineapple ', 'orange', 'grapes', 'banana', 'mango']


lists_2 = ["tomato", "potato", "onion", "carrot", "cabbage"]

# list are mutable -> we can change the value of the list
lists_2[0] = "spinach"
print(lists_2) # ['spinach', 'potato', 'onion', 'carrot', 'cabbage']

# how to iterate over a list
for item in lists_2:
    print(item)