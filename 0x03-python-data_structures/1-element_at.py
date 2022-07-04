#!/usr/bin/python3


def element_at(my_list, idx):
    if idx < 0:
        return None
    j = 0
    for i in my_list:
        if j == idx:
            return i
        j += 1
    return None
