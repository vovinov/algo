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


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
