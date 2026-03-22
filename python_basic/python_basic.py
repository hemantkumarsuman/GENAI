# Variable, datatype, operator, input, output, type casting

# Variable
a = 10
b=20
print(a+b)
print(b)
b = str(b)
print("type of b is: ", type(b))

b = "abc"
print(b)
print("type of b is: ", type(b))

# cannot convert string to int if it is not a number
# b=int(b)
# print(b)

c = 10.5
d = [1, 2, 3, 4, 5 ]
is_valid = True

obj = {
  "name": "Hemant",
  "age": 25
}

print(type(c))
print(type(d))
print(type(obj))
print(type(obj["name"]))
print("name: ", obj["name"])
print(type(is_valid))

# Arithmetic Operators

x = 10
y = 20

print("x + y = ", x+y) #30
print("x - y = ", x-y) #-10
print("x * y = ", x*y) #200
print("y / x = ", y/x)  #2.0 -> division always returns float
print("y // x = ", y//x)  # floor division
print("y % x = ", y%x)  # modulus operator


# Comparison Operators
print("x > y: ", x > y)  # False
print("x < y: ", x < y)  # True 
print("x == y: ", x == y)  # False
print("x != y: ", x != y)  # True
print("x >= y: ", x >= y)  # False
print("x <= y: ", x <= y)  # True


# Logical Operators
print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT

# bitwise operators
print(x & y)  # bitwise AND
print(x | y)  # bitwise OR
print(x ^ y)  # bitwise XOR
print(~x)     # bitwise NOT
print(x << 2) # left shift
print(x >> 2) # right shift
