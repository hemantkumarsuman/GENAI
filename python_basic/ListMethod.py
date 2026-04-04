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