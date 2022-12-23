class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=defaultdict(list)
    def add_edge(self,source,destination):
        self.graph[source].append(destination)
    def print_graph(self):
        for i,j in enumerate(self.graph):
            print(j,"-->",self.graph[j])
          
          
g=Graph(5)

g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(2,3)
g.add_edge(3,4)
g.add_edge(4,0)
g.add_edge(0,4)

g.print_graph()
'''0 --> [1, 4]
   1 --> [2]
   3 --> [4]
   4 --> [0]
   2 --> [3]'''
