import math
import keyword
"""
Write a python comment saying 'Day 2: 30 Days of python programming'
Day 2: 30 Days of python programming
"""
# Write a python comment saying 'Day 2: 30 Days of python programming'
first_name = "Nate"
# Declare a last nae variable and assign a value to it
last_name = "Franklin"
# Declare a full name variable and assign a value to it
fullname = first_name + last_name
# Declare a country variable and assign a value to it
country = "United Kingdom"
# Declare a city variable and assign a value to it
city = "London"
# Declare an age variable and assign a value to it
age = "30"
# Declare a year variable and assign a value to it
year = "2022"
# Declare a variable is_married and assign a value to it
is_married = False
# Declare a variable is_true and assign a value to it
is_true = True
# Declare a variable is_light_on and assign a value to it
is_light_on = is_true
# Declare multiple variable on one line
var1, var2, var3 = 1,2,3

# check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(fullname))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(var1))
print(type(var2))
print(type(var3))
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
print(len(first_name) == len(last_name))
# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5, 4
# Add num_one and num_two and assign the value to a variable total
total = num_two + num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_two - num_one
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
print(product)
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = (math.pi * 30) ** 2
print(area_of_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * 30
print(circum_of_circle)
# Take radius as user input and calculate the area.
radius = input("Please introduce the circle radius: ")
# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input("Please introduce your first name: ")
last_name = input("Please introduce your last name: ")
country = input("Please introduce your country: ")
age = input("Please introduce your age: ")
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
print("----------------------------------------")
print("The list of keywords in python is: ")
for k in keyword.kwlist:
    print(k)
print("----------------------------------------")