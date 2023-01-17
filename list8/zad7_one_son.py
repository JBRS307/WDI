from os import system

class Node:
    def __init__(self, value=None):
        self.val = value
        self.right = None
        self.left = None
#=====================================================

def count(node):
    if node is None:
        return 0
    
    if (node.left is None and node.right is not None):
        return count(node.right)+1
    
    if (node.left is not None and node.right is None):
        return count(node.left)+1

    if node.left is None and node.right is None:
        return 0
    
    if node.left is not None and node.right is not None:
        return count(node.left) + count(node.right)

    
#=====================================================

if __name__ == "__main__":
    system("clear") 