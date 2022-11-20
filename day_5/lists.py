print("########################################")
print("--- LEVEL 1 ---")
print("########################################")


def middle_point(my_list):
    if len(my_list) % 2 ==0:
        return len(my_list) // 2 - 1
    else:
        return len(my_list) // 2


# 1. Declare an empty list
empty_list = []
# 2. Declare a list with more than 5 items
my_list = ["one", "two", "three", "four", "five"]
# 3. Find the length of your list
print(len(my_list))
# 4. Get the first item, the middle item and the last item of the list
print(my_list[0] +", "+ my_list[middle_point(my_list)] + ", "+ my_list[-1])
# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["my_name", 30, 5.9, "single", "my_address"]
# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# 7. Print the list using print()
print(it_companies)
# 8. print the number of companies in the list
print(len(it_companies))
# 9. Print the first, middle and last company
print(it_companies[0] +", "+ it_companies[middle_point(it_companies)] + ", "+ it_companies[-1])
# 10. Print the list after modifying one of the companies
it_companies[0] = "ITC"
print(it_companies)
# 11. Add an IT company to it_companies
it_companies.append("Facebook")
# 12. Insert an IT company in the middle of the companies list
it_companies.insert(middle_point(it_companies), "O2")
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
# 14. Join the it_companies with a string '#; '
print("#; ".join(it_companies))
# 15. Check if a certain company exists in the it_companies list.
print("Facebook" in it_companies)
# 16. sort the list using sort() method
it_companies.sort()
# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
# 18. Slice out the first 3 companies from the list
print(it_companies[0:3])
# 19. Slice out the last 3 companies from the list
print(it_companies[-3:])
# 20. Slice out the middle IT company or companies from the list
print(it_companies[middle_point(it_companies):middle_point(it_companies)+1])
# 21. Remove the first IT company from the list
print(it_companies.pop(0))
# 22. Remove the middle IT company or companies from the list
print(it_companies.pop(middle_point(it_companies)))
# 23. Remove the middle IT company or companies from the list
print(it_companies.pop(len(it_companies)-1))
# 24. Remove all IT companies from the list
print(it_companies.clear())
# 25. Destroy the IT companies list
del it_companies
# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
print(front_end+back_end)
# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end
pos = full_stack.index("Redux")
full_stack.insert(pos+1, "Python")
full_stack.insert(pos+2, "SQL")
print(full_stack)


print("########################################")
print("--- LEVEL 2 ---")
print("########################################")


from countries import countries as cl
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# a. Sort the list and find the min and max age
ages.sort()
print(min(ages))
print(max(ages))
# b. Add the min age and the max age again to the list
ages.append(min(ages))
ages.append(max(ages))
# c. Find the median age (one middle item or two middle items divided by two)
ages.sort()
print(ages[middle_point(ages)])
# d. Find the average age (sum of all items divided by their number )
print(sum(ages)/len(ages))
# e. Find the range of the ages (max minus min)
print(max(ages) - min(ages))
# f. Compare the value of (min - average) and (max - average), use abs() method
min_avg = abs(min(ages) - (sum(ages)/len(ages)))
max_avg = abs(max(ages) - (sum(ages)/len(ages)))
print(min_avg == max_avg)
# 1. Find the middle country(ies) in the countries list
print(cl[middle_point(cl)])
# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
cl1 = cl[0:middle_point(cl)+1]
cl2 = cl[middle_point(cl):]
# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
clist = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_ct, second_ct, third_ct, *scandic = clist
print(first_ct + ", " + second_ct + ", " + third_ct + ", " + str(scandic))
