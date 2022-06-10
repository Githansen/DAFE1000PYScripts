

def Simpsons (f, a, b):
    h = 10**-6
    sum = 0
    sum += (f(a)+f(b)) * h/3
    flip = 0
    a += h
    while a < b:
        if flip % 2 == 0:
            sum += 4*f(a)*h/3
        else:
            sum += 2*f(a)*h/3
        flip +=1
        a += h
    return sum


# h*(f1/2 + f2 + f3 ... + fn/2)
def Trapes (f, a, b):
    h = 10**-6
    sum = 0
    sum += (f(a) + f(b)) * h/2
    a += h
    while a < b:
        sum += h*f(a)
        a = a + h
    return sum


def Rektangel(f,a,b):
    h = 10**-5
    sum = 0
    while a <= b:
        sum += f(a)*h
        a = a+h
    return sum


f = lambda x: 3*x**2
print(Simpsons(f, 0, 2))
print(Rektangel(f, 0, 2))
print(Trapes(f, 0, 2))