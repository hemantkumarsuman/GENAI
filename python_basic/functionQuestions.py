# Function related questions

# celcius to farenheit celcius = temp_value * (9/5) +32
# Farenhiet to celsius

def temperature_convert(temp, type):
    if type == "C":
        tempF = (temp*9/5)+32
        print(f"Temperatuire in Celcius {tempF}")
    elif type == "F":
        tempC = (temp-32)*5/9
        print(f"Temperatuire in Farenheit {tempC}")
    else:
        print(f"Not Valid type")

print(temperature_convert(120,"C"))

# Palindrome 

def palindrome(str):

    str1 = str.lower().replace(" ","");
    if str1==str1[::-1]:
        print(f"Palindrome")
    else:
        print("Not palindrome")

str = "race car"

palindrome(str)

# Calculate total cost of items in cart

cart = [{
    "item1": "Apple",
    "Cost": 100,
    "Quantity": 3
},

{
    "item1": "Banana",
    "Cost": 10,
    "Quantity": 4
},
{
    "item1": "Kiwi",
    "Cost": 45,
    "Quantity": 3
}]
def cartTotal(cart):
    total = 0
    for item in cart:
        print(item)
        total+= item["Cost"]*item["Quantity"]
        
    print(total)


cartTotal(cart)


