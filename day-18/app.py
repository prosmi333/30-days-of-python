import re
# Level 1

# Exercise 1
ans = (6, 'love')

# Exercise 2
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 - (-12)

# Level 2

# Exercise 1


def is_valid_variable(string):
    regex_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
    return bool(re.match(regex_pattern, string))
