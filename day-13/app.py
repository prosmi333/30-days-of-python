numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# Exercise 1

new_num_list = [i for i in range(-4, 6) if i < 0 or i == 0]
print(new_num_list)

# Exercise 2
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

list_of_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flattened = [item
             for sublist in list_of_lists
             for inner in sublist
             for item in inner]
print(flattened)

# Exercise 3
tuples = [
    (i, *[i**exp for exp in range(1, 7)])
    for i in range(11)
]
print(tuples)

# Exercise 4
countries = [
    [('Finland', 'Helsinki')],
    [('Sweden', 'Stockholm')],
    [('Norway', 'Oslo')]
]

country_list = [
    [country.upper(), country[:3].upper(), city.upper()]
    for outer in countries
    for country, city in outer
]
print(country_list)

# Exercise 5

dicts = [
    {'country': country.upper(), 'city': city.upper()}
    for outer in countries
    for country, city in outer
]
print(dicts)

# Exercise 6
names = [
    [('Asabeneh', 'Yetayeh')],
    [('David', 'Smith')],
    [('Donald', 'Trump')],
    [('Bill', 'Gates')]
]
full_names = [
    f"{first} {last}"
    for outer in names
    for first, last in outer
]
print(full_names)
