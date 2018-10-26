def permutations(array):
    if not array:
        return [[]]

    return permute(array)


def permute(arr):
    perms = []
    size = len(arr)
    for i in range(size):
        sub = arr[:]
        swap(sub, 0, i)

        if size > 1:
            for p in permute(sub[1:]):
                p.insert(0, sub[0])
                perms.append(p)
        else:
            return [sub]

    return perms


def swap(arr, a, b):
    temp = arr[b]
    arr[b] = arr[a]
    arr[a] = temp
