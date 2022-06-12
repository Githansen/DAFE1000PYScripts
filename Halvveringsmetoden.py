import math


def halvvering(f, a,b):
    while math.fabs((f(a)+f(b))/2) > 10**-6:
        c = (a+b)/2
        if f(c) > 0:
            a = c
        elif f(c) < 0:
            b = c
    return c


f = lambda x: math.cos(x)-x
print(halvvering(f, 0, 1))