'''
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has
Node.val == val, and return the new head.
'''


class Node():

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


head = Node(1)
b = Node(2)
c = Node(6)
d = Node(3)
e = Node(4)
f = Node(5)
h = Node(6)

head.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = h


def print_list(head):
    res = []
    cur = head
    while cur:
        res.append(cur.value)
        cur = cur.next

    return res


def removeElements(head, val):

    dummy = Node(0, next=head)
    cur = head
    prev = dummy

    while cur:

        if cur.value == val:
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    return dummy.next


print(print_list(removeElements(head, 6)))

print(removeElements([7, 7, 7, 7], 7))
