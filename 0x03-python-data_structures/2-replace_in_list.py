#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    j = 0
    for i in my_list:
        if j == idx:
            my_list[j] = element
            return my_list
        j += 1
    return my_list
