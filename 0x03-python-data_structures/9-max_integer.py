#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        m = my_list[0]
        for i in my_list:
            if m < i:
                m = i
        return m
    else:
        return None
