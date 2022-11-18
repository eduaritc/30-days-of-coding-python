import math

# 1. Declare your age as integer variable
age = 30
# 2. Declare your height as a float variable
height = 5.9
# 3. Declare a variable that store a complex number
complex_number = 25 + 1j
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = input("Enter base: ")
height = input("Enter height: ")
print("The are of the triangle is {}".format(0.5*base*height))
# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = input('Enter side a: ')
side_b = input('Enter side a: ')
side_c = input('Enter side a: ')
print("The perimeter of the triangle is {}".format(side_a + side_b + side_c))
# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = input("Enter length: ")
width = input("Enter width: ")
print("The area of the triangle is {}".format(2*(length + width )))
# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = input("Enter the radius: ")
print("The area of the circle is {}".format(3.14 * (radius**2)))
# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = input("Enter X value: ")
y_intercept = -2
x_intercept = 2
slope_8 = 2 * 2 -2
print("The Y-intercept is {}".format(y_intercept))
print("The X-intercept is {}".format(x_intercept))
print("The slope has a value of {}".format(slope_8))
# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2
x2, y2 = 6, 10
slope_9 = (y1 - y1) / (x2 - x1)
euclidean_distance = math.sqrt(((x1 - y1)**2) + ((x2 - y2)**2))
print("The slope value associated to the points (2,2) ad (6,10) {}".format(slope_9))
print("The euclidean distance betwwen the points (2,2) and (6, 10) is {}".format(euclidean_distance))
# 10. Compare the slopes in tasks 8 and 9.
print(slope_8 == slope_9)
#  11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
a, b, c = 1, 6, 9
discrimiant = b**2 - 4 * a * c
sol1 = (-b - math.sqrt(discrimiant))/(2*a)
sol2 = (-b + math.sqrt(discrimiant))/(2*a)
print("The posible values of Y are: {} and {} ".format(sol1, sol2))
# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") == len("dragon"))
# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")
# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")
# 15. There is no 'on' in both dragon and python
print("on" not in "dragon" and "on" not in "jargon")
# 16.Find the length of the text python and convert the value to float and convert it to string
print(float(len("python")))
print(str(len("python")))
# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = input("Please tell me a number, and I'll tell you if your number is odd or even")
print("is even!" if number % 2 == 0 else "is odd!")
# 18. check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 //2 == int(2.7))
# 19. Check if type of '10' is equal to type of 10
print(type("10") == 10)
# 20. Check if int('9.8') is equal to 10
print(int(9.8) == 10)
# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = input("Enter the hours: ")
rate = input("Enter the rate: ")
print("your weekly earning is {}".format(hours * rate))
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
num_years = input("Enter number of years: ")
print("You've lived for {} seconds".format(num_years * 31556952))
# 23. Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")