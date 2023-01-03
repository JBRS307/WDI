from os import system


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def reverse(self):
        if self.next is None:
            return self
        
        result = self.next.reverse()
        self.next.next = self
        self.next = None
        
        return result
#=====================================================

if __name__ == "__main__":
    system("clear")