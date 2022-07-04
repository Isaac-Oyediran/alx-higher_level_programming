#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0:
        for i in my_list:
            new_list.append(i)
        return new_list
    j = 0
    for i in my_list:
        if j == idx:
            new_list.append(element)
        else:
            new_list.append(i)
        j += 1
    return new_list
