import math


def sum_custom(x):
    lst = []
    for n in x:
        if n.isdigit():
            lst.append(int(n))
    return str(sum(lst))
