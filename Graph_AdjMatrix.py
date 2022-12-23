class Graph:
    def __init__(self,size):
        self.size=size
        self.graph=defaultdict(list)
        self.adjmatrix=[[0 for _ in range(self.size)] for _ in range(self.size) ]
    def add_edge(self,source,destination):
        self.graph[source].append(destination)
        if source==destination:
            return
        self.adjmatrix[source][destination]=1
        self.adjmatrix[destination][source]=1
    def remove_edge(self,source,destination):
        if source==destination:
            return
        adjmatrix[source][destination]=0
        adjmatrix[destination][source]=0
    def __len__(self):
        return self.size
    def print_adjmatrix(self):
        for i in range(len(adjmatrix[source])):
            for j in range(len(adjmatrix[destination])):
                print(j,end="")
            print
            
