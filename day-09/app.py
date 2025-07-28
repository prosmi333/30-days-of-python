# Exercise 1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Exercise 2
your_age = int(input("Enter your age: "))
my_age = 25
if your_age > my_age:
    print(f"You are {your_age - my_age} years older than me.")
elif your_age < my_age:
    print(f"You are {my_age - your_age} years younger than me.")
else:
    print("We are the same age.")

# Exercise 3
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")

# Exercise 4
score = int(input("Enter your score (0–100): "))
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score < 80:
    grade = 'B'
elif 60 <= score < 70:
    grade = 'C'
elif 50 <= score < 60:
    grade = 'D'
elif 0 <= score < 50:
    grade = 'F'
else:
    grade = 'Invalid score'
print("Your grade is:", grade)

# Exercise 5
month = input("Enter month: ").strip().lower()
if month in ['september', 'october', 'november']:
    season = 'Autumn'
elif month in ['december', 'january', 'february']:
    season = 'Winter'
elif month in ['march', 'april', 'may']:
    season = 'Spring'
elif month in ['june', 'july', 'august']:
    season = 'Summer'
else:
    season = 'Invalid month'
print("The season is:", season)

# Exercise 6
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").strip().lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Fruit added. Updated list:", fruits)

# Exercise 7
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 7a
if 'skills' in person:
    print("Middle skill:", person['skills'][len(person['skills']) // 2])

# 7b
if 'Python' in person['skills']:
    print("Python is in the skill set.")

# 7c
skills = person.get('skills', [])
if set(skills) >= {'JavaScript', 'React'}:
    print("He is a front-end developer.")
elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
    print("He is a back-end developer.")
elif set(skills) >= {'React', 'Node', 'MongoDB'}:
    print("He is a full-stack developer.")
else:
    print("Unknown title.")

# 7d
if person['is_married'] and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
