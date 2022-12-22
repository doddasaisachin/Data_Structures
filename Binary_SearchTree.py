class Binary_Search_Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_child(self,data):
        if self.data==data:
            return 
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=Binary_Search_Tree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=Binary_Search_Tree(data)
                
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
        
    def find_min(self):
        Min=self.data
        if self.left:
            Min=self.left.find_min()
        return Min
      
    def find_max(self):
        Max=self.data
        if self.right:
            Max=self.right.find_max()
        return Max
      
    def calculate_sum(self):
        s=0
        s=s+self.data
        if self.left:
            s=s+self.left.calculate_sum()
        if self.right:
            s=s+self.right.calculate_sum()
        return s
      
    def search(self,value):
        if self.data==value:
            return True
        if value<self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value>self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False
       
      
def list_to_binarysearchtree(numbers):
    root=Binary_Search_Tree(numbers[0])
    for num in numbers:
            root.add_child(num)
    return root
