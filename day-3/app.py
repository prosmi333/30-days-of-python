# How tall is big ben?

def estimate_the_height(l, h, L):
    estimated_height = round((h * L) / l)
    print(f"The estimate height of this building is {estimated_height} meters")


estimate_the_height(1.74, 2.51, 66.55)

# Animal name generator


# def name_generator(animal1, animal2, animal3):
# name = slice(animal1, 2) + slice(animal2, 3, 5) + slice(animal3, 4)
# print(f"Suggested name: {name}")

challenge = 'thirty days of python'
print(challenge.capitalize())

# Day 3

# Exercise 1
age = 25
print("Age:", age)

# Exercise 2
height = 1.75  # in meters
print("Height:", height)

# Exercise 3
complex_num = 2 + 3j
print("Complex number:", complex_num)

# Exercise 4
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area_of_triangle = 0.5 * base * height
print("The area of the triangle is:", area_of_triangle)

# Exercise 5
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter_triangle)

# Exercise 6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area of rectangle:", area_rectangle)
print("Perimeter of rectangle:", perimeter_rectangle)

# Exercise 7
radius = float(input("Enter radius: "))
pi = 3.14
area_circle = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of circle:", area_circle)
print("Circumference of circle:", circumference)

# Exercise 8
x = int(input("Enter x value: "))
y = 2 * x - 2
print("y = 2x - 2 =", y)

# Exercise 9
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
euclidean_distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope:", slope)
print("Euclidean distance:", euclidean_distance)

# Exercise 10
slope_1 = 2
print("Slope from question 8:", slope_1)
print("Slope from question 9:", slope)

# Exercise 11
x = -3
y = x**2 + 6*x + 9
print("y = x^2 + 6x + 9 = ", y)

# Exercise 12
print(len("python"))
print(len("dragon"))
print("Length equal:", len("python") == len("dragon"))

# Exercise 13
print("on" in "python" and "on" in "dragon")

# Exercise 14
print("jargon" in "I hope this course is not full of jargon")

# Exercise 15
print("on" not in "python" and "on" not in "dragon")

# Exercise 16
python_length = len("python")
print("Length of 'python':", python_length)
print("Float:", float(python_length))
print("String:", str(python_length))

# Exercise 17
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Exercise 18
print(7 // 3 == int(2.7))

# Exercise 19
print(type('10') == type(10))

# Exercise 20
print(int('9.8') == 10)
