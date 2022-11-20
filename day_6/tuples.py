print("########################################")
print("--- LEVEL 1 ---")
print("########################################")


def get_middle_item(my_collection):
    if len(my_collection) % 2 ==0:
        return len(my_collection) // 2 - 1
    else:
        return len(my_collection) // 2


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

print("########################################")
print("--- LEVEL 2 ---")
print("########################################")


# 1. Unpack siblings and parents from family_members
family_members = tuple(list(siblings) + ["Anna", "Zeus"])
sis1, sis2, sis3, sis4, bro1, bro2, bro3, bro4, *parents = family_members
print("{}, {}, {}, {}, {}, {}, {}, {}, {}, {}"
    .format(
        sis1, sis2, sis3, sis4,
        bro1, bro2, bro3, bro4,
        parents[0], parents[1]))
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("blueberreis", "banana", "mango")
vegetables = ("broccoli",  "coliflower", "carrots")
animal_products = ("eggs", "milk", "cheese")
food_stuff_tp = fruits + vegetables + animal_products
# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_list = list(food_stuff_tp)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print(food_stuff_tp)
print(food_stuff_tp[get_middle_item(food_stuff_tp):get_middle_item(food_stuff_tp)+1])
# 5. Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_tp[0:3]+food_stuff_tp[-3:])
# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp
# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)