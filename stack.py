class Stack:
    def create_empty_stack(self,stack):
        self.stack=[]
    def display(self,stack):
        return self.stack
    def push(self,stack,element):
        self.stack.append(element)
    def pop(self,stack):
        self.stack.pop()
    def isempty(self,stack):
        if len(self.stack)==0:
            return 'TRUE'
        else:
            return 'FALSE'
    def peek(self,stack):
        top=-1
        return self.stack[top]
