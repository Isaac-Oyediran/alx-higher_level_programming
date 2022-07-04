#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix:
        for r in matrix:
            s = ''
            for c in r:
                s += "{:d} ".format(c)
            print(s[:-1])
