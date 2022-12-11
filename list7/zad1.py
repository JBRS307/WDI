from os import system


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head_node=None):
        self.head = head_node
    #-----------------------------------------------------
    def print(self):
        elem = self.head
        while elem is not None:
            print(elem.value, end=" ")
            elem = elem.next
        print()
    #-----------------------------------------------------
    def in_list(self, data):
        elem = self.head
        while elem is not None:
            if elem.value == data:
                return True
        return False
    #-----------------------------------------------------
    def insert_element(self, insert_value, insert_after=None):
        elem = self.head
        new_node = Node(insert_value)
        if insert_after == None:
            new_node.next = elem
            self.head = new_node
        else:
            while elem.next is not None and elem.value != insert_after:
                elem = elem.next
            
            if elem.next is None:
                elem.next = new_node
            else:
                new_node.next = elem.next
                elem.next = new_node
    #-----------------------------------------------------
    def delete_element(self, remove_value):
        elem = self.head
        if elem.value == remove_value:
            self.head = elem.next
            del elem
            return
        
        prev = None
        while elem is not None and elem.value != remove_value:
            prev = elem
            elem = elem.next
        
        if elem is None:
            raise KeyError("Nie ma takiego elementu")
        else:
            prev.next = elem.next
            del elem
            return
#=====================================================

if __name__ == "__main__":
    system("clear")

    test_list = LinkedList(Node(1))
    test_list.insert_element(0)
    test_list.insert_element(3, 1)
    test_list.insert_element(2, 1)
    test_list.insert_element(4, 3)

    test_list.print()
    print()

    test_list.delete_element(5)
    test_list.print()