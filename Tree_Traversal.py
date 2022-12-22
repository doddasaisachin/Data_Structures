class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def inorder(self):
        ele=[]
        if self.left:
            ele=ele+self.left.inorder()
        ele.append(self.data)
        if self.right:
            ele=ele+self.right.inorder()
        return ele
    def preorder(self):
        ele=[]
        ele.append(self.data)
        if self.left:
            ele=ele+self.left.preorder()
        if self.right:
            ele=ele+self.right.preorder()
        return ele
    def postorder(self):
        ele=[]
        if self.left:
            ele=ele+self.left.postorder()
        if self.right:
            ele=ele+self.right.postorder()
        ele.append(self.data)
        return ele
      
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.right.left=Node(8)
root.right=Node(3)
root.right.left=Node(6)
root.right.right=Node(7)
root.right.right.left=Node(9)
root.right.right.right=Node(10)

root.inorder()
#[4, 2, 8, 5, 1, 6, 3, 9, 7, 10]
root.preorder()
#[1, 2, 4, 5, 8, 3, 6, 7, 9, 10]
root.postorder()
#[4, 8, 5, 2, 6, 9, 10, 7, 3, 1]

