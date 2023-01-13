#Zakładam, że usuwam parzyste (2, 4, etc, licząc, że element 1 ma indkes 1)

from os import system


class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
#=====================================================

def remove(elem):
    head = elem
    if elem.next is None:
        return elem
    
    while elem is not None and elem.next is not None:
        elem.next = elem.next.next
        elem = elem.next
    
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

    l1 = Node(1)
    l2 = Node(2)
    l3 = Node(3)
    l4 = Node(4)
    l5 = Node(5)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5

    print_list(l1)
    remove(l1)
    print_list(l1)