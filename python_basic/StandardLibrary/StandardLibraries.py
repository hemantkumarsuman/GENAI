#1) Math Library
from math import *
# Square root
# int_num = int(input("Enter a number: "))
# print("The square root of", int_num, "is", sqrt(int_num))

#2) Random Library -> Used to gnerate random numbers.
import random

print(random.randint(1, 10)) # generates a random integer between 1 and 10 (inclusive)

print(random.choice(['apple', 'banana', 'cherry', 'banana']) )# randomly selects an element from the list

#3) csv Library -> Used to read and write csv files.
# Most of the time we are going to work with csv file.That's why csv library knowledge matters.

import csv
with open('csv_example.txt', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerow(['Alice', 30, 'New York'])
    writer.writerow(['Bob', 25, 'Los Angeles'])
    writer.writerow(['Charlie', 35, 'Chicago'])

with open('csv_example.txt', mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

#4) datetime Library -> Used to work with date and time.
from datetime import datetime,timedelta
current_time = datetime.now()
print("Current date and time:", current_time)

tendays_later = current_time + timedelta(days=10)
print("Date and time after 10 days:", tendays_later)



