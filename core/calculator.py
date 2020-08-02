import math


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def sum_custom(x):
    lst = []
    for n in str(x).split(","):
        if is_digit(n):
            lst.append(int(n))
    return str(sum(lst))


def substract_custom(x):
    lst = []
    for n in str(x).split(","):
        if is_digit(n):
            lst.append(int(n))
    return str(lst[0] - sum(lst[1:]))

