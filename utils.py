import random as rd
import string


def give_me_a_random_phrase(length, level):
    if level == 1:
        letters = string.ascii_lowercase
    elif level == 2:
        letters = string.ascii_letters
    elif level == 3:
        letters = string.ascii_letters + string.digits
    elif level == 4:
        letters = string.ascii_letters + string.digits + string.punctuation
    else:
        letters = "r"

    result_str = ""
    not_long_enough_yet = True

    while not_long_enough_yet:
        intermediate_variable = rd.randint(2, 10)

        for i in range(intermediate_variable):
            if result_str.__len__() == length:
                not_long_enough_yet = False
                break

            result_str += rd.choice(letters)

        if result_str.__len__() < length - 1:
            result_str += " "

    return result_str
