#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0:
        pass
    elif my_list:
        j = 0
        while j < len(my_list):
            if j == idx:
                my_list.remove(my_list[j])
            j += 1
        return my_list
    return my_list
