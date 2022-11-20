# 1. Create an empty tuple
my_tuple = ()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ("Steve", "Bill", "Jeff", "Elon")
sisters = ("Marie", "Judy", "Elsa", "sakura")
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
# 4. How many siblings do you have?
print(len(siblings))
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = tuple(list(siblings) + ["Anna", "Zeus"])
print(family_members)
