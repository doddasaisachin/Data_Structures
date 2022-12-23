import collections
class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=collections.defaultdict(list)
    def add_node(self,data):
        if len(self.graph)<self.size:
            self.graph[data]
        else:
            print('graph size exceeded')
    def add_edge(self,source,destination):
        w=[]
        for node in self.graph:
            w.append(node)
        if source and destination in w:
            self.graph[source].append(destination)
        else:
            print('Nodes are not present in Graph!!')
    def print_nodes(self):
        for node in self.graph:
            print(node,end=" ")
    def print_graph(self):
        for node in self.graph:
            print(node,"-->",self.graph[node])
          
g=Graph(5)

g.add_node(25)
g.add_node(50)
g.add_node(75)
g.add_node(100)
g.add_node(125)

g.add_edge(25,50)
g.add_edge(50,75)
g.add_edge(75,100)
g.add_edge(100,125)
g.add_edge(125,25)
g.add_edge(25,100)

g.print_nodes()
    #25 50 75 100 125

g.print_graph()
''' 25 --> [50, 100]
    50 --> [75]
    75 --> [100]
    100 --> [125]
    125 --> [25]
    20 --> [100]'''
