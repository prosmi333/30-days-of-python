# Exercise 1
from functools import reduce
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
upper_countries = list(map(str.upper, countries))
print("Uppercase countries:", upper_countries)

# Exercise 2
country_name_lengths = list(map(len, countries))
print("Length of each country name:", country_name_lengths)

# Exercise 3
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Exercise 4
land_countries = list(filter(lambda country: 'land' in country, countries))
print("Countries with 'land':", land_countries)

# Exercise 5
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
print("Countries with exactly 6 letters:", six_char_countries)

# Exercise 6
countries_with_e = list(
    filter(lambda country: country.startswith('E'), countries))
print("Countries starting with 'E':", countries_with_e)

# Exercise 7
first_letters = list(
    map(lambda country: country[0],
        filter(lambda country: len(country) > 6, countries))
)
print("First letters of countries with name > 6 chars:", first_letters)

# Exercise 8
sum_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_numbers)

# Exercise 9
all_countries = reduce(lambda x, y: x + ', ' + y, countries)
print("Concatenated countries:", all_countries)

# Exercise 10


def categorize_countries(keyword):
    return [country for country in countries if keyword.lower() in country.lower()]


print("Countries with 'land':", categorize_countries('land'))

# Exercise 11


def country_name_lengths_dict(country_list):
    return [{'country': country, 'length': len(country)} for country in country_list]


print("Country length dicts:", country_name_lengths_dict(countries))

# Exercise 12


def call_function(func, value):
    return func(value)


print(call_function(lambda x: x ** 2, 5))

# Exercise 13


def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


double = make_multiplier(2)
print("Double 10:", double(10))
