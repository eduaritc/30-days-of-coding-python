from countries import countries as cts
from countries_data import countries_data as ctsdata
print("########################################")
print("--- LEVEL 1 ---")
print("########################################")
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
#for loop
# for i in range(11):
#     print(i)

# #while lopp
# i=0
# while i <= 10:
#     print(i)
#     i += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
# for i in range(10, -1, -1):
#     print(i)

# i=10
# while i > -1:
#     print(i)
#     i -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
# for i in range(1, 8):
#     print("#" * i)

# 4. Use nested loops to create the following:
# for i in range(8):
#     for j in range(8):
#         print("# ", end="")
#     print()

#5. Print the following pattern:
# for i in range(11):
#     print("{} x {} = {}".format(i, i, i*i))
    
# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# for item in ['Python', 'Numpy','Pandas','Django', 'Flask']:
#     print(item)

# 7.  Use for loop to iterate from 0 to 100 and print only even numbers
# for i in range(101):
#     print(i) if i % 2 == 0 else i
# 8.  Use for loop to iterate from 0 to 100 and print only odd numbers
# for i in range(101):
#     print(i) if i % 2 != 0 else i

print("########################################")
print("--- LEVEL 2 ---")
print("########################################")
# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# 1.1. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# sum = 0
# sum_even = 0
# sum_odd = 0
# for i in range(101):
#     sum += i
#     if i % 2 == 0:
#         sum_even +=i
#     else:
#         sum_odd +=i
# print("The sum of all numbers is {}".format(sum))
# print("The sum of all evens is {}".format(sum_even))
# print("The sum of all odds is {}".format(sum_odd))

print("########################################")
print("--- LEVEL 3 ---")
print("########################################")

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

# lands = []
# for ct in cts:
#     if "land" in ct:
#         lands.append(ct)
# print(lands)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# reversed_fruits = []
# fruits = ['banana', 'orange', 'mango', 'lemon']
# for i in range(3, -1, -1):
#     reversed_fruits.append(fruits[i])
# print(reversed_fruits)

# 3. Go to the data folder and use the countries_data.py file.

# What are the total number of languages in the data

languages = []
for ctd in ctsdata:
    for l in ctd['languages']:
        if l not in languages:
            languages.append(l)
# print("The number of languages in the world is {}".format(len(languages)))

# Find the ten most spoken languages from the data
# dict_languages = {l: 0 for l in languages}
# for ctd in ctsdata:
#     for l in ctd['languages']:
#         if l in dict_languages.keys():
#             dict_languages[l] += 1 #counting the number of places where every language is spoken

# dict_values = dict_languages.values()
# dict_keys = dict_languages.keys()
# max_count = max(dict_values)
# max_count_pos = list(dict_values).index(max_count)
# print("The most spoken language is {}".format(list(dict_keys)[max_count_pos]))

# Find the 10 most populated countries in the world

#population every country
populations = [country["population"] for country in ctsdata]
#list with the indexes of the most populated countries
indexes_max_populations = []
#top ten number of populations from the population lists
top_ten_pop = sorted(populations, reverse=True)[0:11]
#getting the indexes of the top ten most populated countries
for pop in top_ten_pop:
    indexes_max_populations.append(populations.index(pop))
top_ten_pop_cts = []
#Getting country names associated to the top 10 most populated countries
for i in indexes_max_populations:
    top_ten_pop_cts.append(ctsdata[i]['name'])
print("The top ten most populated countries are: {}".format(top_ten_pop_cts))