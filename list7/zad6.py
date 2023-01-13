from os import system


class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
#=====================================================

def insert(elem, value):
    if elem is None:
        return Node(value)

    head = elem
    head.next = insert(head.next, value)
    return head
#-----------------------------------------------------

def print_list(elem):
    while elem is not None:
        print(elem.val, end=' ')
        elem = elem.next
    print()
#=====================================================

if __name__ == "__main__":
    system("clear")

    l0 = Node(1)
    l1 = Node(12)
    l2 = Node(111111)

    l0.next = l1
    l1.next = l2

    print_list(l0)
    insert(l0, 121)
    print_list(l0)
