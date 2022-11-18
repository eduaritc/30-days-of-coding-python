"""
Elemental mathematical operations
The parameters are used in the order they're being passed to the function. this is,
num1 divided by num2, num1 gets substracted num2, etc.
"""

def addition(num1, num2):
    return num1 + num2
def substraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def module(num1, num2):
    return num1 % num2
def division(num1, num2):
    return num1 / num2
def exponential(num1, num2):
    return num1 ** num2
def floor_division(num1, num2):
    return num1 // num2

print("The sum of {} and {} is: {}".format(1, 2,addition(1, 2)))
print("The result of substractin {} to {} is: {}".format(1, 2,substraction(1, 2)))
print("The result of multiplying {} to  {} is: {}".format(1, 2, multiplication(1, 2)))
print("The remainder of dividing {} by  {} is: {}".format(4, 2, module(4, 2)))
print("The result of dividing {} to  {} is: {}".format(4, 2, division(4,2)))
print("The result of raising {} to a power of  {} is: {}".format(5, 2, exponential(5,2)))
print("The result of dividing {} by  {} is: {}".format(5, 2, floor_division(5, 2)))

"""
Writing a long string on the python console
"""

print("Your name \n your family name \n currently in the UK \n I'm enjoying 30 days of coding")

"""
Checking data types of data
"""
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("your name"))
print(type("your family name"))
print(type("your country"))