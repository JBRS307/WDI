from os import system


class Node:
    def __init__(self, val=None, next=None):
        self.value = val
        self.next = next

class LinkedList:
    def __init__(self, headval=None):
        if headval is None:
            self.head = headval
        else:
            self.head = Node(headval)
    
    def print(self):
        elem = self.head
        while elem is not None:
            print(elem.value, end=' ')
            elem = elem.next
        print()
    
    def append(self, data):
        new_node = Node(data)
        elem = self.head
        if elem is None:
            self.head = new_node
            return

        while elem.next is not None:
            elem = elem.next
        
        elem.next = new_node
#=====================================================

def merge_lists(elem1, elem2):
    res = LinkedList()
    while elem1 is not None and elem2 is not None:
        if elem1.value <= elem2.value:
            res.append(elem1.value)
            elem1 = elem1.next
        else:
            res.append(elem2.value)
            elem2 = elem2.next
    
    if elem1 is None:
        while elem2 is not None:
            res.append(elem2.value)
            elem2 = elem2.next
    
    if elem2 is None:
        while elem1 is not None:
            res.append(elem1.value)
            elem1 = elem1.next
    
    return res
#=====================================================

if __name__ == "__main__":
    system("clear")

    list1 = LinkedList()
    list2 = LinkedList()

    for i in range(1, 30, 2):
        list1.append(i)
    
    for i in range(2, 20, 2):
        list2.append(i)

    list1.print()
    list2.print()

    merged_list = merge_lists(list1.head, list2.head)

    merged_list.print()
