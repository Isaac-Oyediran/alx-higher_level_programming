#!/usr/bin/python3
import hidden_4


def main():
    total = 0
    t = 0
    for i in dir(hidden_4):
        if i[0] == '_' and i[1] == '_':
            pass
        else:
            print("{:s}".format(i))


if __name__ == "__main__":
    main()
