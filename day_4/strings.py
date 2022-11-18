# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty " + "Days " + "Of " + "Python")
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print("Coding " + "For " + "All")
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4. Print the variable company using print().
print(company)
# 5. Print the length of the company string using len() method and print().
print(len(company))
# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())
# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower)
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize() + "\n" + company.title() + "\n" + company.swapcase())
# 9. Cut(slice) out the first word of Coding For All string.
print(company[1:])
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
print(company.rindex("Coding"))
print(company.find("Coding"))
print(company.rfind("Coding"))
print(company.endswith("Coding"))
print(company.count("Coding"))
print("Coding" in company)
# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))
