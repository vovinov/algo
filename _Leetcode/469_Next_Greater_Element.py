from typing import List


def nextGreaterElement1(nums1: List[int], nums2: List[int]) -> List[int]:

    ans = []

    for i in nums1:

        for j in nums2[nums2.index(i) :]:
            if j > i:
                ans.append(j)
                break

        else:
            ans.append(-1)

    return ans


def nextGreaterElement2(nums1, nums2):

    next_greater = {}
    stack = []

    for num in nums2:
        # Пока стек не пуст и текущий элемент больше, чем вершина стека
        while stack and stack[-1] < num:
            # Устанавливаем текущий элемент как следующий больший для вершины стека
            next_greater[stack.pop()] = num
        # Добавляем текущий элемент в стек
        stack.append(num)


# print(nextGreaterElement1([4, 1, 2], [1, 3, 4, 2]))
print(nextGreaterElement2([4, 1, 2], [1, 3, 2, 4]))
