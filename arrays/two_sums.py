def two_sums(array, target):
    dict1 = {}

    for pos, val in enumerate(array):
        diff = target - val
        if diff in dict1:
            first = dict1[diff]
            return [first, pos]
        dict1[val] = pos
