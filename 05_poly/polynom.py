def polyEval(poly, x):
    value = 0
    n = 0
    for coef in poly:
        value += coef * (x ** n)
        n += 1
    return value


def polySum(poly1, poly2):
    poly1_len = len(poly1)
    poly2_len = len(poly2)
    max_len = poly1_len if poly1_len > poly2_len else poly2_len
    result = []

    for i in range(0, max_len):
        j = poly1[i] if i < poly1_len else 0
        k = poly2[i] if i < poly2_len else 0
        result.append(j + k)

    for i in range(max_len - 1, -1, -1):
        if result[i] == 0:
            del result[i]
        else:
            break

    return result


def polyMultiply(poly1, poly2):
    # [1, 2, 5], [2, 0, 1, -7]
    # (1 + 2x + 5x^2) * (2 + 0x + x^2 - 7x^3)
    # (2 + 0x + 1x^2 - 7x^3) + (4x + 0x^2 + 2x^3 - 14x^4) + (10x^2 + 0 + 5x^4 - 35x^5)
    # 2 + 4x + 11x^2 - 5x^3 ...
    #
    #     1   2   5      0  1  2
    # 2   2   4  10   0  0  1  2
    # 0   0   0   0   1  1  2  3
    # 1   1   2   5   2  2  3  4
    # -7 -7 -14 -35   3  3  4  5

    len_x = len(poly1)
    len_y = len(poly2)

    result = [0] * (len_x + len_y - 1)

    for y in range(0, len_y):
        for x in range(0, len_x):
            result[x + y] += poly1[x] * poly2[y]

    return result

