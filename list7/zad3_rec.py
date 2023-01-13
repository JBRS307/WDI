from os import system


class Node:
    def __init__(self, value=None):
        self.val = value
        self.next = None
#=====================================================

def merge(elem1, elem2):
    new_head = Node()
    new_elem = new_head
    def rec(elem1, elem2):
        nonlocal new_elem
                
        if elem1 is None:
            new_elem.next = elem2
            return
        if elem2 is None:
            new_elem.next = elem1
            return
        
        if new_elem.val is not None:
            new_elem.next = Node()
            new_elem = new_elem.next


        if elem1.val < elem2.val:
            new_elem.val = elem1.val
            rec(elem1.next, elem2)
        else:
            new_elem.val = elem2.val
            rec(elem1, elem2.next)
    #-----------------------------------------------------

    rec(elem1, elem2)
    return new_head
#-----------------------------------------------------

def print_list(elem):
    while elem is not None:
        print(elem.val, end=' ')
        elem = elem.next
    print()
#=====================================================

if __name__ == "__main__":
    system("clear")

    l1 = Node(3)
    l2 = Node(7)
    l3 = Node(11)
    l4 = Node(14)
    l1.next = l2
    l2.next = l3
    l3.next = l4

    k1 = Node(4)
    k2 = Node(5)
    k3 = Node(6)
    k4 = Node(20)
    k1.next = k2
    k2.next = k3
    k3.next = k4
    # print_list(k1)

    new_head = merge(k1, l1)

    print_list(new_head)