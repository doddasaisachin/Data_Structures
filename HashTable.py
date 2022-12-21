class hashTable:
    def __init__(self):
        self.max=10
        self.arr=[[] for i in range(self.max)]
        
    def get_hash(self,key):
        h=0
        for char in key:
            h+=ord(char)
        return h%self.max
      
    def __setitem__(self,key,value):
        h=self.get_hash(key)
        found = False
        for index,element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key:
                self.arr[h][index]=(key,value)
                found=True
                break
        if not found:
            self.arr[h].append((key,value))
            
    def __getitem__(self,key):
        h=self.get_hash(key)
        for ele in self.arr[h]:
            if ele[0]==key:
                return ele[1]
              
    def __delitem__(self,key):
        h=self.get_hash(key)
        for idx,ele in enumerate(self.arr[h]):
            if ele[0]==key:
                del self.arr[h][idx]
