from os import system


class Node:
    def __init__(self, value=None):
        self.val = value
        self.left = None
        self.right = None
#=====================================================

def find(node, value):
    if node is None:
        return False
    if node.val == value:
        return True

    return find(node.left) or find(node.right)
#=====================================================

if __name__ == "__main__":
    system("clear")