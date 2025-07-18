# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercise 1
print(len(it_companies))

# Exercise 2
it_companies.add("Twitter")
print(it_companies)

# Exercise 3
it_companies.update(["Alphabet", "Dell Technologies",
                    "Samsung Electronics", "HP Enterprise", "Fujitsu"])
print(it_companies)

# Exercise 4
it_companies.pop()

# Exercise 5
# The difference between remove() and discard() is that remove() makes an error if a the item isn't there while discard doesn't.

# Exercise 6
A.update(B)
print(A)

# Exercise 7
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))

# Exercise 8
print(A.issubset(B))

# Exercise 9
print(A.difference(B))

# Exercise 10
print(A.union(B))
print(B.union(A))

# Exercise 11
print(A.symmetric_difference(B))

# Exercise 12
del A
del B
