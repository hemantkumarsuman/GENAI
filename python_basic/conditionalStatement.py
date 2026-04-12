# Condition statement works like a decision making statement. 
# It allows us to execute certain blocks of code based on certain conditions. 
# The most common conditional statements in Python are if, elif, and else.

# Eligibility for voting
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Comparing height of 3 friends
friend1_height = float(input("Enter height of friend 1 in cm: "))
friend2_height = float(input("Enter height of friend 2 in cm: "))   
friend3_height = float(input("Enter height of friend 3 in cm: "))
if friend1_height > friend2_height and friend1_height > friend3_height:
    print("Friend 1 is the tallest.")
elif friend2_height > friend1_height and friend2_height > friend3_height:
    print("Friend 2 is the tallest.")
else:
    print("Friend 3 is the tallest.")

# Nested if statement

# WHether year is a leap year or not
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")