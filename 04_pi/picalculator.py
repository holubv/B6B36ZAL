import math


def newtonPi(init):
    xk = init
    while True:
        x = xk - (math.sin(xk) / math.cos(xk))
        if x == xk:
            return x
        xk = x


def leibnizPi(iterations):
    pi = 4.0

    j = 3
    k = -1
    for i in range(0, iterations - 1):
        pi += (4 / j) * k
        j += 2
        k *= -1

    return pi


def nilakanthaPi(iterations):
    pi = 3.0

    j = 2
    k = 1
    for i in range(0, iterations - 1):
        pi += (4 / (j * (j + 1) * (j + 2))) * k
        j += 2
        k *= -1

    return pi
