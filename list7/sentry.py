from os import system

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
#=====================================================

def find_key(head, key):
    elem = head
    while elem.value != key:
        if elem.value is None:
            return False
        elem = elem.next
    
    return True
#-----------------------------------------------------

def del_key(elem, sentry, key):
    head = elem
    if elem.value == key:
        return elem

    while elem != elem.next:
        if elem.next.value == key:
            elem.next = elem.next.next
            return head
    return head
#=====================================================

if __name__ == "__main__":
    system("clear")

    head = Node(5)
    e2 = Node(6)
    e3 = Node(9)
    e4 = Node(11)
    sentry = Node()
    head.next = e2
    e2.next = e3
    e3.next = e4
    e4.next = sentry
    sentry.next = sentry

    print(find_key(head, 10))