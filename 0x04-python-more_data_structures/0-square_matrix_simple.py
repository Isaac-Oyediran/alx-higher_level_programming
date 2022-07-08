#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = [[i * i for i in line] for line in matrix]
    return new_matrix
