print("########################################")
print("--- LEVEL 1 ---")
print("########################################")

"""
1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
If below 18 give feedback to wait for the missing amount of years. Output:
"""

# age = input("Enter your age: ")
# if int(age) > 18:
#     print("You're old enough to learn to drive")
# else:
#     print("Please wait for {} years to learn to drive".format(18 - age))

"""
2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) 
to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger
differences, and a custom text if my_age = your_age. Output:
"""

# your_age = input("Enter you age: ")
# if int(your_age) > 30:
#     if int(your_age) - 30 == 1:
#         print("You're {} year older than me".format(1))
#     else:
#         print("You're {} years older than me".format(your_age - 30))
# elif int(your_age) == 30:
#     print("We're same age :')")
# else:
#     if 30 - int(your_age) == 1:
#         print("You're {} year youger than me".format(1))
#     else:
#         print("You're {} years younger than me :')".format(30 - your_age))

"""
3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
if a is less b return a is smaller than b, else a is equal to b. Output:
"""
# a = input("Enter number one: ")
# b = input("Enter number two: ")
# if a > b:
#     print("{} is greater than {}".format(a, b))
# elif a < b:
#     print("{} is smaller than {}".format(a, b))
# else:
#     print("{} is equal to {}".format(a, b))


print("########################################")
print("--- LEVEL 2 ---")
print("########################################")

"""
1. Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
"""
# score = int(input("Enter your score: "))
# if score >= 80 and score <= 100:
#     print("You've got an A")
# elif score >= 70 and score <= 79:
#     print("You've got a B")
# elif score >= 60 and score <= 69:
#     print("You've got a C")
# elif score >= 50 and score <= 59:
#     print("You've got a D")
# elif score >= 0 and score <= 49:
#     print("You've got a F")
# else:
#     print("INVALID SCORE")

"""
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
"""
# month =  input("Enter the current month we're on... ")
# mont = month.lower()
# if month == "september" or month == "october" or month == "november":
#     print("The current season is Autumn!")
# elif month == "december" or month == "january" or month == "february":
#     print("The current season is Winter!")
# elif month == "march" or month == "april" or month == "may":
#     print("The current season is Spring!")
# elif month == "june" or month == "july" or month == "august":
#     print("The current season is Summer!")
# else:
#     print("INVALID MONTH")

"""
3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
"""
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruit = input("Enter a fruit: ")
# if fruit in fruits:
#     print("That fruit already exist in the list")
# else:
#     fruits.append(fruit)
#     print(fruits)


print("########################################")
print("--- LEVEL 3 ---")
print("########################################")

"""
Here we have a person dictionary. Feel free to modify it!
"""
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# print("Exists! :)") if "skills" in person.keys() else print("It doesn't exists! :(")
# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# if "skills" in person.keys() and "Python" in person["skills"]:
#     print("They know Python! :)")
# else:
#     print("They don't know Python! :(")
"""
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, 
 Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),
  else print('unknown title') - for more accurate results more conditions can be nested!
"""
if ["JavaScript", "React"] == person["skills"]:
    print("He is a front end developer")
elif ["Node", "Python", "MongoDB"] == person["skills"]:
    print("He is a backend developer")
elif ["React", "Node", "MongoDB"] == person["skills"]:
    print("He is a fullstack developer")
else:
    print('unknown title')
# * If the person is married and if he lives in Finland, print the information in the following format: Asabeneh Yetayeh lives in Finland. He is married.
if person["is_married"] and person["country"] == "Finland":
    print("{} {} lives in {}. He's married"
    .format(person["first_name"], 
    person["last_name"],
    person["country"]))