class Queue:
    
    def __init__(self):
        self.queue=[]
        self.front=0
        self.rear=-1
        
    def enqueue(self,element):
        self.queue.insert(self.front,element)
        
    def dequeue(self):
        if len(self.queue)>0:
            self.queue.pop()
        else:
            return 'Queue is empty'
        
    def display(self):
        return self.queue
    
    def size(self):
        return len(self.queue)
    
    def last_element(self):
        return self.queue[self.rear]
    
    def front_element(self):
        return self.queue[self.front]
    
    def is_empty(self):
        if len(self.queue)==0:
            return 'TRUE'
        else:
            return 'False'
        
    def peek(self):
        return self.queue[self.front]
