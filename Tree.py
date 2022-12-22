class treenode:
  
    def __init__(self,data):
        self.data=data
        self.children=[]
        self.parent=None
        
    def add_child(self,data):
        data.parent=self
        self.children.append(data)
        
    def get_level(self):
        lev=0
        p=self.parent
        while p:
            lev=lev+1
            p=p.parent
        return lev
      
    def printtree(self):
        prefix=(" " * self.get_level() * 3)+"|--"
        print(prefix+self.data)
        for child in self.children:
            child.printtree()
            
Global=treenode('Global')

india=treenode('india')
usa=treenode('usa')

Global.add_child(india)
Global.add_child(usa)

Gujarath=treenode('Gujarath')
Karnataka=treenode('Karnataka')

india.add_child(Gujarath)
india.add_child(Karnataka)
Gujarath.add_child(treenode('Ahmedabad'))
Gujarath.add_child(treenode('Baroda'))
Karnataka.add_child(treenode('Benguluru'))
Karnataka.add_child(treenode('Mysore'))

NewJersy=treenode('NewJersy')
California=treenode('California')

usa.add_child(California)
usa.add_child(NewJersy)

NewJersy.add_child(treenode('Princeton'))
NewJersy.add_child(treenode('Trenton'))
California.add_child(treenode('SanFrancisco'))
California.add_child(treenode('MountainView'))
California.add_child(treenode('PaloAlto'))

Global.printtree()

