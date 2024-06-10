
def climbing_stairs(n):
    one = 1
    two = 0

    for i in range(n):
        temp = one
        one = one + two
        two = temp
    return one


print(climbing_stairs(5))