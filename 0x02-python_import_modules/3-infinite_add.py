#!/usr/bin/python3
from sys import argv


def main():
    total = 0
    t = 0
    for i in argv:
        if t > 0:
            total += int(i)
        t += 1
    print(total)


if __name__ == "__main__":
    main()
