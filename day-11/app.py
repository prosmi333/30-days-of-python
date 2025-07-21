# Exercise 1
def add_two_numbers(a, b):
    return a + b

# Exercise 2


def area_of_circle(radius):
    pi = 3.14159
    return pi * radius ** 2

# Exercise 3


def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "Only numbers are allowed"
    return total

# Exercise 4


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Exercise 5


def check_season(month):
    month = month.lower()
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month'

# Exercise 6


def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Exercise 7


def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        root1 = (-b + discriminant ** 0.5) / (2 * a)
        root2 = (-b - discriminant ** 0.5) / (2 * a)
        return (root1, root2)

# Exercise 8


def print_list(lst):
    for item in lst:
        print(item)

# Exercise 9


def reverse_list(lst):
    return lst[::-1]

# Exercise 10


def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]

# Exercise 11


def add_item(lst, item):
    lst.append(item)
    return lst

# Exercise 12


def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# Exercise 13


def sum_of_numbers(n):
    return sum(range(n + 1))

# Exercise 14


def sum_of_odds(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# Exercise 15


def sum_of_even(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)

# Level 2
# Exercise 1


def evens_and_odds(n):
    evens = sum(1 for i in range(n + 1) if i % 2 == 0)
    odds = n + 1 - evens
    print(f"The number of odds are {odds}")
    print(f"The number of evens are {evens}")


# Exercise 2


def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Exercise 3


def is_empty(data):
    return not bool(data)

# Exercise 4


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]


def calculate_mode(numbers):
    from collections import Counter
    count = Counter(numbers)
    max_freq = max(count.values())
    mode = [k for k, v in count.items() if v == max_freq]
    return mode[0] if len(mode) == 1 else mode


def calculate_range(numbers):
    return max(numbers) - min(numbers)

# Exercise 5


def calculate_stats(numbers):
    return {
        'mean': calculate_mean(numbers),
        'median': calculate_median(numbers),
        'mode': calculate_mode(numbers),
        'range': calculate_range(numbers)
    }

# Level 3
# Exercise 1


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Exercise 2


def is_unique(lst):
    return len(lst) == len(set(lst))

# Exercise 3


def is_valid_variable(name):
    import keyword
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    return True


# Exercise 4
# The built-in Python function `all()` checks if all items in an iterable are true.
print(all([True, 1, "non-empty"]))
print(all([True, 0, "hello"]))


def custom_all(iterable):
    for item in iterable:
        if not item:
            return False
    return True
