#Siwocha Lukasz
#Cw. 10
#Python


import random
import numpy


def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a % b)


def power(a, b):
    result = 1
    for i in numpy.arange(b):
        result = result * a
    return result


def solve_DL(a, n):
    r = 1
    while (power(a, r) % n != 1 and r < 10):
        r += 1
    if (r == 10):
        return -1
    else:
        return r


def factorize(n):
    random_number = round(random.random() * 100000000) % n

    if (GCD(n, random_number) > 1):
        print(f"N: {n}, NWD: {GCD(n, random_number)}")
    else:
        r = solve_DL(random_number, n)
        print(f"R: {r}")
        if (r == -1):
            factorize(n)
        elif (r % 2 == 0):
            if (GCD(n, power(random_number, r / 2) + 1) > 1):
                print(f"N: {n}, POTEGA: {power(random_number, r / 2) + 1}")
            elif (GCD(n, power(random_number, r / 2) - 1) > 1):
                print(f"N: {n}, POTEGA: {power(random_number, r / 2) - 1}")
            else:
                factorize(n)
        else:
            factorize(n)


factorize(12)
factorize(91)
factorize(143)
factorize(1737)
factorize(1859)
factorize(988027)