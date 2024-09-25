def flipAndInvertImage(image):

    for row in image:

        l, r = 0, len(row) - 1

        while l <= r:

            row[l], row[r] = row[r], row[l]

            row[l] = 0 if row[l] else 1

            if l != r:
                row[r] = 0 if row[r] else 1

            l += 1
            r -= 1

    return image


print(
    flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
)  # [[1,0,0],[0,1,0],[1,1,1]]
