from numbers import *


def start():
    print("""
    Hi, welcome to LGP's:
    [1] - Pharmacy
    [2] - Perfumery
    [3] - Cosmetics
    """)


def choose_an_option():
    user_option = int(input("Choose an option: "))
    return user_option


user_option = 0
x = generate_numbers_pharmacy()
y = generate_numbers_perfumery()
z = generate_numbers_cosmetics()
while user_option != 4:
    start()
    user_option = choose_an_option()
    if user_option == 1:
        print_number((next(x)))
    elif user_option == 2:
        print_number((next(y)))
    elif user_option == 3:
        print_number((next(z)))
print("See you later")