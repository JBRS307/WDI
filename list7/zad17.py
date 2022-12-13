from os import system
# from random import randrange


class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, initval=None):
        if initval is None:
            self.head = self.tail = None
        else:
            self.head = self.tail = Node(initval)
    
    def print(self):
        elem = self.head
        if elem is None:
            print("List is empty")
            return
        while elem is not None:
            print(elem.value, end=' ')
            elem = elem.next
        print()
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = self.tail.next
    
    def remove(self):
        if self.head is None:
            return
        if self.head.next is None:
            if odd_ones(self.head.value):
                self.head = self.tail = None
        
        while odd_ones(self.head.value) and self.head is not None:
            self.head = self.head.next

        elem = self.head.next
        while elem is not None:
            if odd_ones(elem.value):
                if elem.prev is not None:
                    elem.prev.next = elem.next
                if elem.next is not None:
                    elem.next.prev = elem.prev
            elem = elem.next
#=====================================================

def odd_ones(num):
    num = bin(num)
    res = 0
    for dig in num:
        if dig == '1':
            res += 1
    
    return res%2 == 1
#-----------------------------------------------------

def delete(list1):
    if list1.head is None:
        return
    if list1.head.next is None:
        if odd_ones(list1.head.value):
            list1.head = None
        return
    
    while odd_ones(list1.head.value) and list1.head is not None:
        list1.head = list1.head.next
    
    elem = list1.head.next
    while elem is not None:
        if odd_ones(elem.value):
            if elem.prev is not None:
                elem.prev.next = elem.next
            if elem.next is not None:
                elem.next.prev = elem.prev
        elem = elem.next
#=====================================================

if __name__ == "__main__":
    system("clear")

    list1 = LinkedList()
    # for _ in range(20):
    #     list1.append(randrange(1, 30))

    for i in range(1, 21):
        list1.append(i)
    
    # list1.append(2)
    # list1.remove()

    delete(list1)

    list1.print()