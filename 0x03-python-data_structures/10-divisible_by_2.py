#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list:
        j = 0
        new_list = []
        while j < len(my_list):
            if my_list[j] % 2 == 0:
                new_list.append(1)
            else:
                new_list.append(0)
            j += 1
        return new_list
    else:
        return None
