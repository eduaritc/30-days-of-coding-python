import math
from countries_data import countries_data as ctsdata
print("########################################")
print("--- LEVEL 1 ---")
print("########################################")


# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_number(num1, num2):
    return num1+num2

# 2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return 3.14 * radius ** 2

#  3. Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for n in nums:
        total += n
    return total

# 4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(centigrados):
    return centigrados * (9/5) + 32

#5. Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month == "september" or month == "october" or month == "november":
        return("Autumn")
    elif month == "december" or month == "january" or month == "february":
        return("Winter")
    elif month == "march" or month == "april" or month == "may":
        return("Spring")
    elif month == "june" or month == "july" or month == "august":
        return("Summer")
    else:
        return("INVALID MONTH")

# 6. Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 -x1)

# 7. Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    solutions = []
    discriminant = b**2 - 4 * a * c
    print(discriminant)
    sol1 = (-b - math.sqrt(discriminant))/(2*a)
    sol2 = (-b + math.sqrt(discriminant))/(2*a)
    solutions.extend([sol1, sol2])
    return solutions

# 8. Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(p_list):
    for l in p_list:
        print(l)

# 9. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(normal_list):
    rev_list = []
    for i in range(len(normal_list)-1, -1, -1):
        rev_list.append(normal_list[i])
    return rev_list
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

# 10. Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(uncapitalist):
    capitalist = []
    for item in uncapitalist:
        capitalist.append(item.capitalize())
    return capitalist

#11. Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(my_list, item):
    my_new_list = my_list.copy()
    my_new_list.append(item)
    return my_new_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))

# 12. Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(my_list, item):
    one_item_less = my_list.copy()
    one_item_less.remove(item)
    return one_item_less

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# 13. Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# 14. Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum_odds = 0
    for i in range(1, num+1):
        if i % 2 != 0:
            sum_odds +=i
    return sum_odds

# 15. Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(num):
    sum_evens = 0
    for i in range(num+1):
        if i % 2 == 0:
            sum_evens +=i
    return sum_evens

print("########################################")
print("--- LEVEL 2 ---")
print("########################################")

# 1. Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    num_evens = 0
    num_odds = 0
    for i in range(num+1):
        if i % 2 == 0:
            num_evens += 1
        else:
            num_odds += 1
    print("The number of evens is {}".format(num_evens))
    print("The number of odds is {}".format(num_odds))

evens_and_odds(100)

# 2. Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

# 3. Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    return is_empty(param)

# 4. Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation).

def calculate_mean(my_list):
    return sum(my_list)/len(my_list)

def middle_point(my_list):
    if len(my_list) % 2 ==0:
        return len(my_list) // 2 - 1
    else:
        return len(my_list) // 2

def calculate_median(my_list):
    my_list.sort()
    return middle_point(my_list)

def calculate_mode(my_list):
    max_count = 0
    for item in my_list:
        if my_list.count(item) > max_count:
            max_count = item
    return max_count

def calculate_range(my_list):
    return max(my_list) - min(my_list)

def calculate_variance(my_list):
    parcial_variance = 0
    mean = calculate_mean(my_list)
    for item in my_list:
        parcial_variance += (item - mean) ** 2
    return parcial_variance/len(my_list)

def calculate_std(my_list):
    return math.sqrt(calculate_variance(my_list))

print("########################################")
print("--- LEVEL 3 ---")
print("########################################")    

# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(number):
    prime = True
    for i in range(2, number//2):
        if number % i == 0:
            prime = False
    return prime

# 2. Write a functions which checks if all items are unique in the list.
def unique_list(my_list):
    is_unique = True
    for item in my_list:
        if my_list.count(item) > 1:
            is_unique = False
            break
    return is_unique

# 3. Write a function which checks if all the items of the list are of the same data type.
def all_data_same_type(my_list):
    all_the_same = True
    type_item = type(my_list[0]).__name__
    for i in range(1, len(my_list)):
        if type(my_list[i]).__name__ != type_item:
            all_the_same = False
            break
    return all_the_same
print(all_data_same_type(["1",2,3,4]))

# 4. Write a function which check if provided variable is a valid python variable
def valid_variable(variable):
    return variable.isidentifier()

# 5. Go to the data folder and access the countries-data.py file.
# a. Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

def most_spoken_languages():
    languages = []
    for ctd in ctsdata:
        for l in ctd['languages']:
            if l not in languages:
                languages.append(l)

    dict_languages = {l: 0 for l in languages}
    for ctd in ctsdata:
        for l in ctd['languages']:
            if l in dict_languages.keys():
                dict_languages[l] += 1 #counting the number of places where every language is spoken
    top_20_spkn_langs = dict(sorted(dict_languages.items(), key=lambda item: item[1], reverse = True)[0:21])
    return list(top_20_spkn_langs.keys())
    # print("The most spoken languages are: {}".format(list(top_20_spkn_langs.keys())))
# most_spoken_languages()

# 5.b.Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries():
    #population every country
    populations = [country["population"] for country in ctsdata]
    #list with the indexes of the most populated countries
    indexes_max_populations = []
    #top ten number of populations from the population lists
    top_20_pop = sorted(populations, reverse=True)[0:21]
    #getting the indexes of the top ten most populated countries
    for pop in top_20_pop:
        indexes_max_populations.append(populations.index(pop))
    top_20_pop_cts = []
    #Getting country names associated to the top 10 most populated countries
    for i in indexes_max_populations:
        top_20_pop_cts.append(ctsdata[i]['name'])
    # print("The top 20 most populated countries are: {}".format(top_20_pop_cts))
    return top_20_pop_cts
most_populated_countries()
