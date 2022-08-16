# Moak data
test_list = [10, 6, 4, 8, 7, 2, 3, 22, 31, 11, 66]


def bubble_sort(data):
    length = len(data)
    for i in range(length):
        for n in range(length - 1 - i):
            if data[n] > data[n + 1]:
                data[n], data[n + 1] = data[n + 1], data[n]
    return data
