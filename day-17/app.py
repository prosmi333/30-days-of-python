# Exercise 1
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
# Unpack first five into nordic_countries, and 'Estonia', 'Russia' into es, ru
nordic_countries, es, ru = names[:5], names[5], names[6]
print(nordic_countries, es, ru)
