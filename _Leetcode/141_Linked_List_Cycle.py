class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


a = Node(3)
b = Node(2)
c = Node(0)
d = Node(-4)


a.next = b
b.next = c
c.next = d
d.next = b


def out(head):
    elems = []
    cur = head

    while cur:
        elems.append(cur.val)
        cur = cur.next

    return elems


def is_cycle1(head):

    seen = set()

    while head:

        if head in seen:
            return True

        seen.add(head)

        head = head.next

    return False


def is_cycle2(head):

    if not head:
        return False

    slow = head
    fast = head.next

    while fast and fast.next:

        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False


print(is_cycle1(a))
print(is_cycle2(a))
