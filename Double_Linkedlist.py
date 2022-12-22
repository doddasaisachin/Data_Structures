class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
        
class linkedlist:
  
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        new_node=Node(data)
        temp=self.head
        if self.head is not None:
            temp.prev=new_node
        new_node.next=temp
        self.head=new_node
        
    def insert_at_end(self,data):
        itr=self.head
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        while itr.next is not None:
            itr=itr.next
        itr.next=node
        node.prev=itr
        
    def sizeof_linkedlist(self):
        if self.head is None:
            print('empty linked list')
        c=0
        itr=self.head
        while itr is not None:
            c=c+1
            itr=itr.next
        return c
      
    def insert_at_index(self,data,index):
        if index<0 or index>=self.sizeof_linkedlist():
            raise Exception('index error')
        node=Node(data)
        c=0
        itr=self.head
        while itr:
            if (c==index-1):
                node.next=itr.next
                itr.next=node
                node.prev=itr
                break
            c=c+1
            itr=itr.next
            
    def insert_after(self,prev,data):
        node=Node(data)
        if prev is None:
            print('previos node cant be null')
            return
        node.next=prev.next
        prev.next=node
        node.prev=prev
        
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,'-->',end="")
            temp=temp.next
            
    def delete_node(self,node):
        if self.head is None or node is None:
            print('Empty linked list')
            return
        if node == self.head:
            self.head=node.next
        if node.next is not None:
            node.next.prev=node.prev
        if node.prev is not None:
            node.prev.next=node.next
            
    def delete_by_value(self,value):
        if self.head is None :
            print('linked list is empty')
            return 
        itr=self.head
        while itr:
            if (int(itr.data)==int(value)):
                if itr.next is not None:
                    itr.next.prev=itr.prev
                if itr.prev is not None:
                    itr.prev.next=itr.next
            itr=itr.next
            
    def sort_linkedlist(self):
        if self.head is None:
            print('linked list is empty')
        itr=self.head
        temp=None
        while itr:
            temp=itr.next
            while temp:
                if(int(temp.data)<int(itr.data)):
                    temp.data,itr.data=itr.data,temp.data
                temp=temp.next
            itr=itr.next
        return self.display()
