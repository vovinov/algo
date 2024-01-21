
class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


a = Node(1)
b = Node(2)
c = Node(4)

d = Node(1)
e = Node(3)
f = Node(4)

a.next = b
b.next = c

d.next = e
e.next = f

def out(head):
    elems = []
    cur = head

    while cur:
        elems.append(cur.val)
        cur = cur.next

    return elems


def merge(list1, list2):
    start = Node()
    cur = start

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    if list1:
        cur.next = list1
    if list2:
        cur.next = list1
    return start.next


print(out(a))
print(out(d))
print(merge(a,d))


