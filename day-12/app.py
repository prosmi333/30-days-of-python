# Level 1
# Exercise 1
import string
import random


def random_user_id(color, fruit, animal, word):
    first_letters = color[0:1]
    second_two_letters = fruit[0:3]
    third_two_letters = animal[-1:-3]
    last_letter = word[-1]
    print(
        f"Your user id is: {first_letters+second_two_letters+third_two_letters+last_letter}")


random_user_id("blue", "dragonfruit", "penguin", "ishak")


# Exercise 2


# def user_id_gen_by_user():
#     x = 0
#     characters_in_id = input("How many characters should your id have?: ")
#     ids_to_gen = input("How many ids do you want?: ")
#     print(characters_in_id, ids_to_gen)
#     characters = string.ascii_letters + string.digits + string.punctuation
#     while x < ids_to_gen:
#         for i in range(characters_in_id):
#             gen_id = ''.join(random.choice(characters))
#             print(gen_id)
#         x = + 1


# user_id_gen_by_user()

# Exercise 3


def rgb_colr_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print(f"rgb({red},{green},{blue})")


rgb_colr_gen()

# Level 2
# Exercise 1


def list_of_hexa_colors(num):
    hexa_color = str(random.randint(0, 9)) + \
        random.choice(string.ascii_letters) + str(random.randint(0, 9)) + \
        random.choice(string.ascii_letters) + str(random.randint(0, 9)) + \
        random.choice(string.ascii_letters)
    print(f"[#{hexa_color}]")


list_of_hexa_colors(3)

# Exercise 2


def list_rgb_colr_gen(num):
    x = 0
    list_of_colors = []
    while x < num:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        list_of_colors.append(f"rgb({red},{green},{blue})")
        x += 1
    print(list_of_colors)


list_rgb_colr_gen(5)

# Exercise 3


def generate_colors(type, num):
    if type == "rgb":
        list_rgb_colr_gen(num)
    elif type == "hexa":
        list_of_hexa_colors(num)
    else:
        print("The parameters are faulty. Please make sure the type is a string.")


generate_colors("rgb", 6)
