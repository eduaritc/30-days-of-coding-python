print("########################################")
print("--- LEVEL 1 ---")
print("########################################")
from random import random, randint
import random as arbitrary
import string
# 1. Writ a function which generates a six digit/character random_user_id.

def random_user_id():
    alphabet = string.ascii_letters + string.digits
    user_id = []
    for i in range(6):
        random_pos = randint(0, len(alphabet)-1)
        user_id.append(alphabet[random_pos])
    return "".join(user_id)
# random_user_id()


"""
2. . Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
 One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""


def user_id_gen_by_user():
    num_characters = input("Enter number of characters: ")
    num_ids = input("Enter number of ID's to generate: ")
    alphabet = string.ascii_letters + string.digits
    user_id = []
    user_ids = []
    for i in range(int(num_ids)):
        for j in range(int(num_characters)):
            random_pos = randint(0, len(alphabet)-1)
            user_id.append(alphabet[random_pos])
        user_ids.append("".join(user_id))
    return user_ids
# print(user_id_gen_by_user()) # 5 5
# print(user_id_gen_by_user()) # 16 5


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    colors = [randint(0, 255) for i in range(3)]
    output = "rgb({},{},{})".format(colors[0], colors[1], colors[2])
    return output
# rgb_color_gen()

print("########################################")
print("--- LEVEL 2 ---")
print("########################################")


"""
1. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after 
#. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
"""

def list_of_hexa_colors(num_colors):
    alphabet = string.digits+"abcdef"
    list_colors = []
    for i in range(num_colors):
        color = ["#"]
        for j in range(6):
            pos_digit = randint(0, 15)
            [color.append(alphabet[pos_digit])]
        list_colors.append("".join(color))
    return(list_colors)
# list_of_hexa_colors(3)

# 2. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num_colors):
    list_colors = []
    for i in range(num_colors):
        color = [randint(0, 255) for i in range(3)]
        list_colors.append("rgb({},{},{})".format(color[0], color[1], color[2]))
    print(list_colors)
# list_of_rgb_colors(3)

# 3. Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(hexa_rgb, num):
    if hexa_rgb == "hexa":
        list_of_hexa_colors(num)
    else:
        list_of_rgb_colors(num)

# generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
# generate_colors('hexa', 1) # ['#b334ef']
# generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
# generate_colors('rgb', 1)  # ['rgb(33,79, 176)']


print("########################################")
print("--- LEVEL 3 ---")
print("########################################")

# 1. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(my_list):
    arbitrary.shuffle(my_list)
# fruits = ["apple", "banana", "cherry"]
# shuffle_list(fruits)
# print(fruits)

# 2. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random_nums():
    rand_numbers = []
    while len(rand_numbers) < 7:
        num = randint(0, 9)
        if num not in rand_numbers:
            rand_numbers.append(num)
    return rand_numbers

# random_numbers = seven_random_nums()
# print(random_numbers)
        
        


