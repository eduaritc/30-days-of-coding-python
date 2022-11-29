from functools import reduce
from countries import countries as cts
from countries_data import countries_data as cts_data
import string

print("###########################################")
print("### --- LEVEL 1 --- ###")
print("###########################################")


"""
1. Explain the difference between map, filter and reduce:
    --> Maps: Iterate over a list applying the function passed as parameter to every item; it returns an iterable
    --> Filter: It's a map where the final result are all of those items that satisfy a condition, such
    condition is defined at the function passed as first parameter (filter criteria); it returns an iterable
    --> Reduce: it's like a map, with the difference that it returns a single value, plus it's not a built-in function anymore
            it has to be importe in the module functools
    -->Differences: 
            --> Maps and filters receive an iterable and a function, return another iterable,  but the filter "filter" the elements 
            of the iterable which the function is applied to, by other hand, reduce isn't a built-in function anymore and it returns just one value
"""

"""
2. Explain the difference between higher order function, closure and decorator.
    --> Higher order functions: they contain other functions as a parameter or return a function as an output.
    properties:
         --> A function is an instance of the object type.
         --> You can store the function in a variable.
         --> You can pass the function as a parameter to another function.
         --> You can return the function from another function.
         --> You can store them in data structures such as hash tables, lists, etc.
    --> Closures: nested functions, where the inner function has acces to the outer scope and 
        is returned as result of the outer function.
    --> decorators: Design pattern that allows an user to add new funcionality to an existing function object
    wihout modifying its structure. Usually called before the definiton of the function you want to decorate.
    it needs of an outer function with an inner wrapper function.
    -->Differences: 
            --> They three all return another function as result, but in a higher order function, this functions is
            not inside of it, whereas in closures and decorators, the returned function is inside of them.
            --> Closures and Decorators have access to the outer scope, whereas higher order functions don't.
"""
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # 3. Define a call function before map, filter or reduce, see examples
# def product(num1, num2):
#     return num1 * num2
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# def add_seven(number):
#     return number + 7

# list_numbers_plus_seven = map(add_seven, numbers)
# list_even_numbers = filter(is_even, numbers)
# prod_numbers_list = reduce(product, numbers)
# print("------------------Numbers plus seven-------------------------")
# [print(x) for x in list_numbers_plus_seven]
# print("-------------------------------------------------------------")
# print("------------------Even numbers plus seven--------------------")
# [print(x) for x in list_even_numbers]
# print("-------------------------------------------------------------")
# print("------Sum of all of the numbers in the list------------------")
# print(prod_numbers_list)
# print("-------------------------------------------------------------")

# # 4. user for loop to print each country in the countries list
# print("------countries------------------")
# [print(country) for country in countries]
# print("-------------------------------------------------------------")
# # 5. use for to print each name in the names list
# print("------names------------------")
# [print(name) for name in names]
# print("-------------------------------------------------------------")
# # 6. Use for to print each number in the numbers list
# print("------numbers------------------")
# [print(num) for num in numbers]
# print("-------------------------------------------------------------")

print("###########################################")
print("### --- LEVEL 2 --- ###")
print("###########################################")

# # 1. Use map to create a new list by changin each country to uppercase in the countries list
# upper_countries = map(lambda country: country.upper(), countries)
# print("------------------------Countries----------------------------")
# [print(country) for country in upper_countries]
# print("-------------------------------------------------------------")

# # 2. use map to creat a new list b changing each number to its square inthe number lists
# squares = map(lambda num: num ** 2, numbers)
# print("------------------------Squares----------------------------")
# [print(sqr) for sqr in squares]
# print("-------------------------------------------------------------")

# # 3. use map to change each name to uppercase in the names list
# upper_names = map(lambda name: name.upper(), names)
# print("------------------------Countries----------------------------")
# [print(name) for name in upper_names]
# print("-------------------------------------------------------------")

# # 4. Use filter to tilter out countries containing 'land'.
# lands = filter(lambda land: "land" in land, countries)
# print("------------------------Lands----------------------------")
# [print(land) for land in lands]
# print("-------------------------------------------------------------")

# # 5. use filter to filter out countries having exactly six characters
# six_letters_countries = filter(lambda country: len(country) == 6, countries)
# print("-------------------six letters countries---------------------")
# [print(country) for country in six_letters_countries]
# print("-------------------------------------------------------------")

# #6. Use filter to filter out countries containing six letter and more in the contry list
# six_letters_and_more_countries = filter(lambda country: len(country) >= 6, countries)
# print("---------------six letters and more countries------------------")
# [print(country) for country in six_letters_and_more_countries]
# print("-------------------------------------------------------------")

# # 7. Use filter to filter out countries starting with an "E"
# ecountries = filter(lambda country: country[0] == "E", countries)
# print("------------------------Countries----------------------------")
# [print(country) for country in ecountries]
# print("-------------------------------------------------------------")

# # 8. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# chained_lists = reduce(lambda x, y: x[0] + y[0] ,filter(lambda c: "LAND" in c, map(lambda c: c.upper(), countries)))
# print("------------------------chained lists----------------------------")
# [print(element) for element in chained_lists]
# print("-------------------------------------------------------------")

# # 9. Declare a function called get_string_lists which takes a list as a parameter and the returns a list containing only string items
# def get_string_lists(lst):
#     str_list = list(filter(lambda x: type(x).__name__ == "str", lst))
#     return str_list
# print("------------------------Strings only----------------------------")
# print(get_string_lists(countries+numbers))
# print("-------------------------------------------------------------")


# # 10 use reduce to sum all the number in the numbers list
# print("------------------------SUM of List----------------------------")
# print(reduce(lambda x, y: x + y, numbers))
# print("-------------------------------------------------------------")


# """
# use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden,
# Denmark, Norway, and Iceland are north European Countries
# """ 
# def european_countries(c1, c2):
#     if c2.lower() != "iceland":
#         return c1 + ", " +c2
#     else:
#         return c1 + ", and " +c2 + " are north European countries"

# print("------------------------EUROPEAN COUNTRIES----------------------------")
# print(reduce(european_countries, countries))
# print("-------------------------------------------------------------")

# """
#  12. declare a function called categorize_countries that returns a list of countries with some common pattern
#  you can find the countries list in this repository as countires.js (eg 'land', 'ia', 'island', 'stan')
# """
# def categorize_countries(countries, pattern):
#     return (list(filter(lambda c: pattern in c.lower(), countries)))

# print("-----------------lands----------------------------")
# print(categorize_countries(cts, "land"))
# print("-----------------ias----------------------------")
# print(categorize_countries(cts, "ia"))
# print("-----------------islands----------------------------")
# print(categorize_countries(cts, "island"))
# print("-----------------stans----------------------------")
# print(categorize_countries(cts, "stan"))
# print("-----------------sps----------------------------")
# print(categorize_countries(cts, "sp"))
# print("-----------------cols----------------------------")
# print(categorize_countries(cts, "col"))
# print("-------------------------------------------------------------")

"""
# 13. Create a function returning a dictionary, where keys stand for starting letter of countries and values
are the number of country names starting with that letter
"""

# def num_stand_cts(countries):
#     alphabet = list(string.ascii_lowercase)
#     dict_cts = {}
#     for letter in alphabet:
#         list_countries_stand_letters = list(filter(lambda ct: letter == ct[0].lower(), cts))
#         dict_cts[letter] = len(list_countries_stand_letters)
#     return dict_cts
# print(num_stand_cts(cts))

# 14. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# def get_first_ten_countries():
#     return cts[0:11]
# print(get_first_ten_countries())

# 15. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
# def get_last_ten_countries():
#      return cts[-10:]
# print(get_last_ten_countries())

print("###########################################")
print("### --- LEVEL 3 --- ###")
print("###########################################")

#FOR COUNTRIES BY NAME
# countries_name_index = {cts_data[i]["name"] : i for i in range(len(cts_data)) }
# countries = sorted(countries_name_index.keys())
# countries_by_name = [cts_data[countries_name_index[countries[i]]] for i in range(len(cts_data))]
# print("-----------------------COUNTRIES BY NAME-------------------------------")
# [print(country) for country in countries_by_name]
# print("-----------------------------------------------------------------------")

#FOR COUNTRIES BY CAPITAL
# countries_capital_index = {cts_data[i]["capital"] if cts_data[i]["capital"] else cts_data[i]["name"] : i for i in range(len(cts_data)) }
# capitals = sorted(countries_capital_index.keys())
# print(str(len(capitals)) + " " + str(len(cts_data)))
# countries_by_capital = [cts_data[countries_capital_index[capitals[i]]] for i in range(len(capitals))]
# print("-----------------------COUNTRIES BY CAPITAL----------------------------")
# [print(country) for country in countries_by_capital]
# print("----------------------------------------------------------------------")

#FOR COUNTRIES BY population
# countries_population_index = {cts_data[i]["population"]: i for i in range(len(cts_data)) }
# populations = sorted(countries_population_index.keys())
# print(str(len(populations)) + " " + str(len(cts_data)))
# countries_by_population = [cts_data[countries_population_index[populations[i]]] for i in range(len(populations))]
# print("-----------------------COUNTRIES BY POPULATION----------------------------")
# [print(country) for country in countries_by_population]
# print("----------------------------------------------------------------------")

# 2. The ten most spoken languages
# LIST COMPREHENSION APPROACH NOT FULLY WORKING, BUT I'M CLOSE
# languages = []
# languages = [cts_data[i]["languages"][0] if len(cts_data[i]["languages"]) <= 1 else languages.extend(cts_data[i]["languages"]) for i in range(len(cts_data)-1)]
# languages = [list().extend(cts_data[i]["languages"]) for i in range(len(cts_data))]
# langs_count = {lang: languages.count(lang) for lang in languages}
# print(langs_count)
#REGULAR LIST CREATION
# languages = []
# for data in cts_data:
#     if len(data["languages"]) == 1:
#         languages.append(data["languages"][0])
#     else:
#         languages.extend(data["languages"])
# langs_count = {lang: languages.count(lang) for lang in languages}
# print(sorted(langs_count.items(), reverse = True, key=lambda item: item[1])[0:11])

# 3. Sort out the ten most populated coutries
# countries_population_index = {cts_data[i]["population"]: i for i in range(len(cts_data)) }
# populations = sorted(countries_population_index.keys())
# print(str(len(populations)) + " " + str(len(cts_data)))
# countries_by_population = [cts_data[countries_population_index[populations[i]]] for i in range(len(populations))]
# print(countries_by_population[-10:])