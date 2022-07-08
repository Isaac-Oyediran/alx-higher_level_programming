#!/usr/bin/python3


def search_replace(my_list, search, replace):
    my_matrix = []
    for i in my_list:
        if i == search:
            my_matrix.append(replace)
        else:
            my_matrix.append(i)
    return my_matrix
