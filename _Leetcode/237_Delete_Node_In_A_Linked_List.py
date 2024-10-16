class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(4)
b = ListNode(5)
c = ListNode(1)
d = ListNode(9)

a.next = b  # type: ignore
b.next = c  # type: ignore
c.next = d  # type: ignore


def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
