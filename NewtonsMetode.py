import math
import Derivert
import pandas


def newtonsukjentderivert(f, x):
    xgammel = x-1
    while x-xgammel > 10**-10:
        xgammel = x
        x = x-f(x)/Derivert.main(f, x)
    return x


def newtons(f, fd, x):
    xgammel = x-1
    while x-xgammel > 10**-10:
        xgammel = x
        x = x - f(x)/fd(x)
    return x


## Funksjon og den deriverte
f = lambda x: math.cos(x)-x
fd = lambda x: -math.sin(x)-1


