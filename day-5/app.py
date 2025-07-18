# Exercise 1
empty_list = []

# Exercise 2
companies = ['Facebook', 'Google', 'Microsoft',
             'Apple', 'Shein', 'Ebay', 'Amazon']

# Exercise 3
print("Length of the list:", len(companies))

# Exercise 4
print("First company:", companies[0])
print("Middle company:", companies[len(companies) // 2])
print("Last company:", companies[-1])

# Exercise 5
mixed_data_types = ['Asabeneh', 250, True, {'country': 'Finland'}]
print("Mixed data types:", mixed_data_types)

# Exercise 6
it_companies = ['Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon']

# Exercise 7
print("IT Companies:", it_companies)

# Exercise 8
print("Number of IT companies:", len(it_companies))

# Exercise 9
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

# Exercise 10
it_companies[0] = 'Meta'
print("After change:", it_companies)

# Exercise 11
it_companies.append('Spotify')
print("After append:", it_companies)

# Exercise 12
it_companies.insert(len(it_companies) // 2, 'Intel')
print("After insert:", it_companies)

# Exercise 13
print("Company with uppercase:", [company.upper() for company in it_companies])

# Exercise 14
print("#; ".join(it_companies))

# Exercise 15
print("Is 'Amazon' in list?", 'Amazon' in it_companies)

# Exercise 16
it_companies.sort()
print("Sorted:", it_companies)

# Exercise 17
it_companies.sort(reverse=True)
print("Reversed sorted:", it_companies)

# Exercise 18
print("First 3 companies:", it_companies[:3])

# Exercise 19
print("Last 3 companies:", it_companies[-3:])

# Exercise 20
mid_index = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    print("Middle companies:", it_companies[mid_index - 1: mid_index + 1])
else:
    print("Middle company:", it_companies[mid_index])

# Exercise 21
it_companies.pop(0)
print("After removing first:", it_companies)

# Exercise 22
it_companies.pop(mid_index)
print("After removing middle:", it_companies)

# Exercise 23
it_companies.pop()
print("After removing last:", it_companies)

# Exercise 24
it_companies.clear()
print("After clearing:", it_companies)

# Exercise 25
del it_companies
