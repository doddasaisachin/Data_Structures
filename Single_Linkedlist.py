class Node:
    
    def __init__(self,data=None,Next=None):
        self.data=data
        self.Next=Next
        
class linkedlist:
    
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.Next:
            itr=itr.Next
        itr.Next=Node(data,None)
        
    def prinT(self):
        if self.head is None:
            print("linked list is empty")
        itr=self.head
        while itr:
            print(itr.data,"-->",end="")
            itr=itr.Next
            
    def insert_after(self,prev_node,data):
        if prev_node is None:
            print('Node must be in Linked list')
        node=Node(data,prev_node.Next)
        prev_node.Next=node
        
    def insert_list(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
            
    def sizeof_linkedlist(self):
        c=0
        itr=self.head
        while itr:
            c=c+1
            itr=itr.Next
        return c
    
    def deleteat_value(self,value):
        if self.head.data==value:
            self.head=self.head.Next
        itr=self.head
        while itr:
            if (self.head is not None):
                if itr.Next.data==value:
                    itr.Next=itr.Next.Next
                    break
                itr=itr.Next
                
    def deleteat_index(self,index):
        if index<0 or index>=self.sizeof_linkedlist():
            raise Exception("invalid index")
        if index==0:
            self.head=self.head.next
        c=0
        itr=self.head
        while itr:
            if c==index-1:
                itr.Next=itr.Next.Next
                break
            itr=itr.Next
            c=c+1
            
    def search_key(self,key):
        if self.head is None:
            print('linked list is empty')
        if (self.head is not None):
            itr=self.head
            while itr:
                if itr.data==key:
                    return True
                itr=itr.Next
            return False
        
    def sort_linkedlist(self):
        itr=self.head
        next=None
        if self.head is None:
            print('linked list is empty')
        while itr is not None:
            next=itr.Next
            while next is not None:
                if int(itr.data)>int(next.data):
                    itr.data,next.data=next.data,itr.data
                next=next.Next
            itr=itr.Next
