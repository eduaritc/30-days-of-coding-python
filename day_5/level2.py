from countries import countries as cl
def middle_point(my_list):
    if len(my_list) % 2 ==0:
        return len(my_list) // 2 - 1
    else:
        return len(my_list) // 2
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