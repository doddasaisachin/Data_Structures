class Graph(object):
    def __init__(self,Vertices):
        self.Vertices=Vertices
        self.graph=[]
    def add_edge(self,sour,dest,dis):
        self.graph.append([sour,dest,dis])
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return find(parent,parent[i])
    def apply_union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        if rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
    def kruskals_algo(self):
        parent=[]
        rank=[]
        result=[]
        i,e=0,0
        self.graph=sorted(self.graph,key=lambda x : x[2])
        for node in range(self.Vertices):
            parent.append(node)
            rank.append(0)
        while e<self.Vertices-1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                result.append([u,v,w])
                e=e+1
                self.apply_union(parent,rank,x,y)
        for a,b,c in result:
            print("%d - %d : %d " %(a,b,c))
            
g=Graph(6)
g.add_edge(0,1,4)
g.add_edge(0,2,4)
g.add_edge(1,2,2)
g.add_edge(1,0,4)
g.add_edge(2,0,4)
g.add_edge(2,1,2)
g.add_edge(2,3,3)
g.add_edge(2,5,2)
g.add_edge(2,4,4)
g.add_edge(3,2,3)
g.add_edge(3,4,3)
g.add_edge(4,2,4)
g.add_edge(4,3,3)
g.add_edge(5,2,2)
g.add_edge(5,4,3)
g.kruskals_algo()
'''
    1 - 2 : 2 
    2 - 5 : 2 
    2 - 3 : 3 
    3 - 4 : 3 
    0 - 1 : 4 
'''
