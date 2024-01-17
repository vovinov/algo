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


def reverse(head):
    cur = head
    prev = None

    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev


print(reverse(a))
print(out(e))

# print(out(a))





