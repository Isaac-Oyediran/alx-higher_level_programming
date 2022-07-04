#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        j = 0
        for i in my_list:
            j += 1
        j -= 1
        for i in my_list:
            print("{:d}".format(my_list[j]))
            j -= 1
