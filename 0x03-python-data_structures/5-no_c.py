#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    j = 0
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string += i
            j += 1
    return new_string
