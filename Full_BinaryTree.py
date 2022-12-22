class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def IsFullBinaryTree(self):
        if root is None:
            return True
        if self.left is None and self.right is None:
            return True
        if self.left is not None and self.right is not None:
            return self.left.IsFullBinaryTree() and self.right.IsFullBinaryTree()
        
        return False
    
root=Node(1)

root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(6)
root.left.right.right=Node(7)

root.IsFullBinaryTree()
#True
