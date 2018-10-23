def sortNumbers(weights, condition):
    return sort(weights, condition)


def sortData(weights, data, condition):
    size = len(weights)
    size_data = len(data)
    if size != size_data:
        raise ValueError('Invalid input data')

    def move_data(arr, a, b):
        move(arr, a, b)
        move(data, a, b)

    sort(weights, condition, move_data)
    return data


def sort(arr, mode, move_fn=None):
    if not move_fn:
        move_fn = move

    size = len(arr)

    # for i in range(size):
    #    for j in range(size - 1, i - 1, -1):
    #        if compare(arr[i], arr[j], mode):
    #            swap_fn(arr, i, j)

    value = None
    index = -1

    for i in range(size):
        for j in range(i, size):
            if value is None or compare(value, arr[j], mode):
                value = arr[j]
                index = j

        move_fn(arr, index, i)
        value = None

    return arr


def compare(a, b, mode):
    return a < b if mode == 'DESC' else a > b


def move(arr, f, t):
    value = arr[f]
    del arr[f]
    arr.insert(t, value)
    return arr

