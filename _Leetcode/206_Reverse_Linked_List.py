from copy import deepcopy


class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


a = Node(2)
b = Node(8)
c = Node(3)
d = Node(-1)
e = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e


def out(head):
    elems = []
    cur = head
    while cur:
        elems.append(cur.val)
        cur = cur.next
    return elems


print(out(a))


def reverse(head):

    prev = None
    nextp = None
    cur = head

    while cur:
        nextp = cur.next
        cur.next = prev
        prev = cur
        cur = nextp

    return prev


prev = reverse(a)
print(out(prev))
