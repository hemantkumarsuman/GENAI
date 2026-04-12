# looping statement is used to execute a block of code repeatedly until a certain condition is met.

# For loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.

# Range() -> It is a built-in function that generates a sequence of numbers. 
# It can take one, two, or three arguments: start, stop, and step.

# Print  1 to 50
# for i in range(1,51):
#     print(i)

# print 1 to 100 with gap of 5
# for i in range(1,101,5):
#     print(i)

# print 100 to 1 with gap of 5
for i in range(100,-1,-5):
    print(i)

# in loopint statement, we can iterate over a string, list, tuple, set, dictionary etc.
name = "Hemant Kumar"
for i in name:
    # print(i)

# While loop is used to execute a block of code repeatedly as long as a certain condition is true.
#print even number between 1 to 50

num = 0 
while(num<=50):
    if num%2==0:
        print(num)
    else :
        pass
    num+=1


# Loop control statements are used to control the flow of execution in a loop.
# 1) break -> It is used to exit the loop when a certain condition is met.
# 2) continue -> It is used to skip the current iteration and move to the next iteration when a certain condition is met.
# 3) pass -> It is used as a placeholder for future code. It does nothing 
#    and is used when a statement is required syntactically but no code needs to be executed.


