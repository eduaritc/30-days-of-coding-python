print("########################################")
print("--- LEVEL 1 ---")
print("########################################")


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Find the length of the set it_companies
print(len(it_companies))
# 2. Add 'Twitter' to it_companies
it_companies.add("twitter")
# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(["ITC", "TESLA"], "DELL")
# 4. Remove one of the companies from the set it_companies
print(it_companies.pop())
# 5.What is the difference between remove and discard
# Discard doesn't raise any error when the element to remove isn't found


print("########################################")
print("--- LEVEL 2 ---")
print("########################################")


# 1. Join A and B
print(A.union(B))
# 2. Find A intersection B
print(A.intersection(B))
# 3. Is A subset of B
print(A.issubset(B))
# 4. Are A and B disjoint sets
print(A.isdisjoint(B))
# 5. Join A with B and B with A
print("AuB --> {}; BuA --> {}".format(A.union(B), B.union(A)))
# 6. What is the symmetric difference between A and B
print(A.symmetric_difference(B))
# 7. Delete the sets completely
del A, B


print("########################################")
print("--- LEVEL 3 ---")
print("########################################")

# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(type(age_set))
# 2. Explain the difference between the following data types: string, list, tuple and set
"""
Strings are anyting enclose between double or single quotes and are immutables
List by other hand is a colletion of elements of any type and are mutable
tuples are immutable lists
sets could be defined as lists or tuples that don't admmit repeated elements with unordere values
"""
# 3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
phrase = "I am a teacher and I love to inspire and teach people"
print(len(set(phrase.split(" "))))
