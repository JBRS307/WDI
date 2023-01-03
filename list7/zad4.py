from os import system


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
#=====================================================

def reverse_list(elem):
    if elem is None:
        return None
    
    head = elem
    next_elem = head.next

    if next_elem is None:
        return head
    
    result = reverse_list(next_elem.next)
    next_elem.next = head

    return result
    
#=====================================================

if __name__ == "__main__":
    system("clear")