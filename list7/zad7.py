from os import system


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
#=====================================================

def remove_last(elem):
    if elem is None:
        return None
    
    head = elem
    next_elem = elem.next

    if next_elem is None:
        return None
    else:
        head.next = remove_last(next_elem)
        return head    
#=====================================================

if __name__ == "__main__":
    system("clear")