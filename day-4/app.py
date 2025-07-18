# Exercise 1
print("Thirty " + "Days " + "Of " + "Python")

# Exercise 2
print("Coding " + "For " + "All")

# Exercise 3
company = "Coding For All"

# Exercise 4
print(company)

# Exercise 5
print(len(company))

# Exercise 6
print(company.upper())

# Exercise 7
print(company.lower())

# Exercise 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Exercise 9
print(company[0:6])  # first word

# Exercise 10
print(company.find("Coding"))

# Exercise 11
print(company.replace("Coding", "Python"))

# Exercise 12
print(company.split())

# Exercise 13
company2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company2.split(", "))

# Exercise 14
print(company[0])  # first character

# Exercise 15
print(company[-1])  # last character

# Exercise 16
print(company[10])  # character at index 10

# Exercise 17
acronym = ''.join([word[0] for word in "Python For Everyone".split()])
print(acronym)

# Exercise 18
acronym2 = ''.join([word[0] for word in "Coding For All".split()])
print(acronym2)

# Exercise 19
print(company.index('C'))

# Exercise 20
print(company.index('F'))

# Exercise 21
print(company.rfind('l'))

# Exercise 22
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# Exercise 23
print(sentence.rindex('because'))

# Exercise 24
print(sentence[sentence.index('because'):sentence.rindex('because')+7])

# Exercise 25
print(company.startswith("Coding"))
print(company.endswith("All"))

# Exercise 26
print(company.strip(" "))

# Exercise 27
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# Exercise 28
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

# Exercise 29
print("I am enjoying this challenge.\nI just wonder what is next.")

# Exercise 30
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Exercise 31
radius = 10
area = 3.14 * radius ** 2
print(
    f"The area of a circle with radius {radius} is {int(area)} meters square.")

# Exercise 32
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
