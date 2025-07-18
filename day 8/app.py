# Exercise 1
dog = {}

# Exercise 2
dog = {
    'name': 'Buddy',
    'color': 'Brown',
    'breed': 'Labrador',
    'legs': 4,
    'age': 5
}

# Exercise 3
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript'],
    'country': 'Canada',
    'city': 'Toronto',
    'address': '123 Main St'
}

# Exercise 4
print("Length of student dictionary:", len(student))

# Exercise 5
print("Skills:", student['skills'])
print("Data type of skills:", type(student['skills']))

# Exercise 6
student['skills'].append('React')
student['skills'].append('SQL')
print("Updated skills:", student['skills'])

# Exercise 7
print("Keys:", student.keys())

# Exercise 8
print("Values:", student.values())

# Exercise 9
print("Items:", student.items())

# Exercise 10
student.pop('marital_status')
print("After removing 'marital_status':", student)

# Exercise 11
del dog
# print(dog)  # Would raise NameError if uncommented
