#!/usr/bin/python3
for i in range(0, 10):
    for digit in range(i + 1, 10):
        if i == 8 and digit == 9:
            print("{}{}".format(i, digit))
        else:
            print("{}{}".format(i, digit), end=", ")
