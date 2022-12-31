class Graph(object):
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[]
        self.adj_mat=[[0 for i in range(self.vertices)] for j in range(self.vertices)]
    def add_edge(self,sou,dest,w):
        self.graph.append([sou,dest,w])
        self.adj_mat[sou][dest]=w
        self.adj_mat[dest][sou]=w

g=Graph(6)
g.add_edge(0,1,2)
g.add_edge(0,2,4)
g.add_edge(1,2,3)
g.add_edge(1,5,3)
g.add_edge(5,3,1)
g.add_edge(3,2,6)
g.add_edge(2,4,8)

inf=99999999999
selected=[None for _ in range(g.vertices)]
E=0
import random
selected[random.randint(0,g.vertices-1)]=True 
while E<g.vertices-1:
    x,y=0,0
    Min=inf
    for i in range(g.vertices):
        if selected[i]:
            for j in range(g.vertices):
                if ((not selected[j]) and g.adj_mat[i][j]):
                    if Min>g.adj_mat[i][j]:
                        Min=g.adj_mat[i][j]
                        x,y=i,j
    print(f"{str(x)} - {str(y)} : {str(g.adj_mat[x][y])}" )
    E=E+1
    selected[y]=True
