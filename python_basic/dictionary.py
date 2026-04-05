# Dictionary is a collection which is unordered, changeable and indexed. 
# In Python dictionaries are written with curly brackets, and they have keys and values.

# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "Mumbai"}
print(my_dict) # {'name': 'John', 'age': 30, 'city': 'Mumbai'}

# Accessing values in a dictionary
print(my_dict["name"]) # John

# Adding a new key-value pair to the dictionary
my_dict["country"] = "INDIA"

print(my_dict) # {'name': 'John', 'age': 30, 'city': 'Mumbai', 'country': 'INDIA'}

# Updating the value of an existing key
my_dict["age"] = 31
print(my_dict) # {'name': 'John', 'age': 31, 'city': 'Mumbai', 'country': 'INDIA'}

# Removing a key-value pair from the dictionary
del my_dict["city"]
print(my_dict) # {'name': 'John', 'age': 31, 'country': 'INDIA'}

#Adding a new key-value pair to the dictionary
my_dict["city"] = "Mumbai"
print(my_dict) # {'name': 'John', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}

###### Dictionary methods

# keys() -> it returns a list of all the keys in the dictionary
print(my_dict.keys()) # dict_keys(['name', 'age', 'country'])

# How to iterate through the keys of a dictionary
for key in my_dict.keys():
    print(key)

# values() -> it returns a list of all the values in the dictionary
print(my_dict.values()) # dict_values(['John', 31, 'INDIA', 'Mumbai'])

# items() -> it returns a list of all the key-value pairs in the dictionary
print(my_dict.items()) # dict_items([('name', 'John'), ('age', 31), ('country', 'INDIA'), ('city', 'Mumbai')])

# get() -> it returns the value of the specified key
print(my_dict.get("name")) # John
print(my_dict.get("city")) # Mumbai
print(my_dict.get("")) # None


# Shallow copy of a dictionary

# we can copy a dictionary using = operator but it creates a reference to the original dictionary
my_dict_ref_copy = my_dict
print(my_dict_ref_copy) # {'name': 'John', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}
my_dict_ref_copy["name"] = "Jane"
print(my_dict_ref_copy) # {'name': 'Jane', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}
print(my_dict) # {'name': 'Jane', 'age': 31, 'country   : 'INDIA', 'city': 'Mumbai'}

# To create a copy of a dictionary we can use the copy() method which creates a shallow copy of the dictionary i.e 
# it creates a new dictionary with the same key-value pairs as the original dictionary but 
# it does not create a reference to the original dictionary.

my_dict_copy = my_dict.copy()
print(my_dict_copy) # {'name': 'John', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}

my_dict_copy["name"] = "Jane"
print(my_dict_copy) # {'name': 'Jane', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}
print(my_dict) # {'name': 'John', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}

my_dict["age"] = 25

print(my_dict) # {'name': 'John', 'age': 25, 'country': 'INDIA', 'city': 'Mumbai'}
print(my_dict_copy) # {'name': 'Jane', 'age': 31, 'country': 'INDIA', 'city': 'Mumbai'}


# nested dictionary -> it is a dictionary that contains another dictionary as a value
nested_dict = {
    "name": "John",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Mumbai",
        "country": "INDIA"
    }
}

print(nested_dict) # {'name': 'John', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Mumbai', 'country': 'INDIA'}}

# Iterating through a nested dictionary

for outer_key, outer_value in nested_dict.items():
    print("Outer key:", outer_key)
    print("Outer value:", outer_value)
    if isinstance(outer_value, dict):
        for inner_key, inner_value in outer_value.items():
            print("Inner key:", inner_key)
            print("Inner value:", inner_value)