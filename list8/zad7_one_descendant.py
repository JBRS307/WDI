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
        if node.right.left is None and node.right.right is None:
            return 1
        else:
            return count(node.right)
    
    if (node.left is not None and node.right is None):
        if node.left.left is not None and node.left.right is not None:
            return 1
        else:
            return count(node.left)

    if node.left is None and node.right is None:
        return 0
    
    if node.left is not None and node.right is not None:
        return count(node.left) + count(node.right)

    
#=====================================================

if __name__ == "__main__":
    system("clear") 