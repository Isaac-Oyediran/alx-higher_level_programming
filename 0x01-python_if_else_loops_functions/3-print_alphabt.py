#!/usr/bin/python3
for ch in range(ord('a'), ord('z') + 1):
    if ch != ord('e') and ch != ord('q'):
        print("{}".format(chr(ch)), end="")
