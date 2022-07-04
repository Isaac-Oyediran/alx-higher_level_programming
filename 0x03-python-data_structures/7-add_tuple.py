#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    arr = [0, 0]
    j = 0
    for i in tuple_a:
        if j == 0:
            arr[0] += i
        if j == 1:
            arr[1] += i
        if j > 1:
            break
        j += 1
    j = 0
    for i in tuple_b:
        if j == 0:
            arr[0] += i
        if j == 1:
            arr[1] += i
        if j > 1:
            break
        j += 1
    t = (arr[0], arr[1],)
    return t
