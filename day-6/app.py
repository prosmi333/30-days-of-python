# Exercise 1
empty_tuple = ()

# Exercise 2
sisters = ('Aisha', 'BellyBaby', 'BellyBaby2')
brothers = ('Papa', 'Shmuunu', 'BellyBaby')

# Exercise 3
siblings = sisters + brothers
print("Siblings:", siblings)

# Exercise 4
print("Number of siblings:", len(siblings))

# Exercise 5
family_members = siblings + ('Mama', 'Daddy')
print("Family members:", family_members)

# Exercise 6
siblings = family_members[:-2]
parents = family_members[-2:]
print("Siblings:", siblings)
print("Parents:", parents)

# Exercise 7
fruits = ('apple', 'banana', 'mango')
vegetables = ('carrot', 'cucumba', 'spinach')
animal_products = ('chicken', 'egg', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products
print("Food tuple:", food_stuff_tp)

# Exercise 8
food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)

# Exercise 9
mid_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    print("Middle items:", food_stuff_lt[mid_index - 1:mid_index + 1])
else:
    print("Middle item:", food_stuff_lt[mid_index])

# Exercise 10
food_stuff_lt = food_stuff_lt[3:-3]
print("After removing first and last 3 items:", food_stuff_lt)

# Exercise 11
del food_stuff_tp
# print(food_stuff_tp)  # Would raise NameError if uncommented

# Exercise 12
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Is 'Estonia' a Nordic country?", 'Estonia' in nordic_countries)
print("Is 'Iceland' a Nordic country?", 'Iceland' in nordic_countries)
