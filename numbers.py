def generate_numbers_pharmacy():
    number = 0
    while number >= 0:
        number += 1
        yield f"PH {number}"


def generate_numbers_perfumery():
    number = 0
    while number >= 0:
        number += 1
        yield f"PE {number}"


def generate_numbers_cosmetics():
    number = 0
    while number >= 0:
        number += 1
        yield f"CO {number}"


def decorate(f_to_be_decorated):
    def inner_function(*args):
        print("Your number is:")
        f_to_be_decorated(*args)
        print("Pay attention, please.")
    return inner_function

@decorate
def print_number(number_to_print):
    print(number_to_print)
