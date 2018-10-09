import math


def addition(x, y):
    return x + y


def subtraction(x, y):
    return x - y


def multiplication(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x / y


def modulo(x, y):
    if x < y or y <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return x % y


def secondPower(x):
    return x * x


def power(x, y):
    if y < 0:
        raise ValueError('This operation is not supported for given input parameters')
    return math.pow(x, y)


def secondRadix(x):
    if x <= 0:
        raise ValueError('This operation is not supported for given input parameters')
    return math.sqrt(x)


def magic(x, y, z, k):
    l = x + k
    m = z + y
    if m == 0:
        raise ValueError('This operation is not supported for given input parameters')
    return (l / m) + 1


def control(a, x, y, z, k):
    args = [x, y, z, k]
    fnMap = {
        'ADDITION': (addition, 2),
        'SUBTRACTION': (subtraction, 2),
        'MULTIPLICATION': (multiplication, 2),
        'DIVISION': (division, 2),
        'MOD': (modulo, 2),
        'POWER': (power, 2),
        'SECONDRADIX': (secondRadix, 1),
        'MAGIC': (magic, 4)
    }
    fn_type = fnMap.get(a)
    if not fn_type:
        raise ValueError('This operation is not supported for given input parameters')

    fn = fn_type[0]
    arg_len = fn_type[1]
    return fn(*args[:arg_len])
