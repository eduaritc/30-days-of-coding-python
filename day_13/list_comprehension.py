# 1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
zero_negatives = [x for x in numbers if x <= 0]
print(zero_negatives)

# 2. flatten the following list of list of list to a one dimensional list.
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flatten_list_of_lists = [z for y in list_of_lists for z in y for x in y  for z in x ]
print(flatten_list_of_lists)

# 3. using list comprehension to create the followin list of tuples
squares = [(x, 1, x**1, x**2, x**3, x**4, x**5) for x in range(7)]
print(squares)

# 4.flatten the following list to a new list.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_capitals = [[country_cap_tup[0], country_cap_tup[0][0:3], country_cap_tup[1]] for country_cap_lst in countries for country_cap_tup in country_cap_lst ]
print(countries_capitals)

# 5.change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list_dict = [ {"country":country_cap_tup[0], "city": country_cap_tup[1]} for country_cap_lst in countries for country_cap_tup in country_cap_lst ]
print(list_dict)

# 6. change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
fullnames = [name_surname_tup[0]+" "+name_surname_tup[1] for name_surname_lst in names for name_surname_tup in name_surname_lst]
print(fullnames)

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slopes_y_intercept = [("x = " + str(x), "y = " + str(2* x + 3)) for x in range(10)]
print(slopes_y_intercept)
