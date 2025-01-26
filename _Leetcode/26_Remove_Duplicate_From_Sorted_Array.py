def removeDuplicates(nums):

    one = 0
    two = 1

    while two < len(nums):

        if nums[two] == "_":
            return two

        if nums[two] == nums[one]:
            del nums[two]
            nums.append("_")
        else:
            one += 1
            two += 1


def removeDuplicates2(nums):

    j = 0

    for i in range(len(nums)):

        if nums[i] != nums[j]:
            j += 1
            nums[i], nums[j] = nums[j], nums[i]

    return j + 1


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates2([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
