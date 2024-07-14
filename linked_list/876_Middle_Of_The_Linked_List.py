"""
Given the head of a singly linked list,
return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Ex 1
"""
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e
"""

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f


def middleNode1(node):  # [1,2,3,4,5]
    res = []
    counter = 0
    cur = node

    while cur:
        res.append(cur.val)
        cur = cur.next
        counter += 1

    middle = counter // 2

    cur = node
    while cur:
        if middle == 0:
            return cur.val
        middle -= 1
        cur = cur.next


def middleNode2(node):  # [1,2,3,4,5,6]

    counter = 0

    cur = node

    while cur:
        cur = cur.next
        counter += 1

    middle = counter // 2

    cur = node
    while cur:
        if middle == 0:
            return cur.val
        middle -= 1
        cur = cur.next


# print(middleNode1(a))
print(middleNode2(a))
