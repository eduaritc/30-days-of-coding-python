# 1. Create an empty dictionary called dog
dog = {}
# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {
    "name": "Zeus",  
    "color": "Black",
    "breed": "Bulldog",
    "legs": 4,
    "age": 7 
    }
# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Oliver",
    "last_name": "Atom",
    "gender": "Male",
    "age": 17,
    "martial_status": "Single",
    "skills": ["football", "tennis", "maths" "science"],
    "country": "United Kingdom",
    "city": "London",
    "address": "123, false streect"
}
# 4. Get the length of the student dictionary
print(len(student))
# 5. Get the value of skills and check the data type, it should be a list
print(student["skills"])
# 6. Modify the skills values by adding one or two skills
student["skills"].extend(["Physics", "Software Engineering"])
print(student["skills"])
# 7. Get the dictionary keys as a list
print(student.keys())
# 8. Get the dictionary values as a list
print(student.values())
# 9. Change the dictionary to a list of tuples using items() method
print(student.items())
# 10. Delete one of the items in the dictionary
print(list(student.items()).pop(0))
# 11. Delete one of the dictionaries
del dog




