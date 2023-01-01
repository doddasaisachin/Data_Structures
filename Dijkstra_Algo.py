class Graph(object):
    def __init__(self,vertices):
        self.vertices=vertices
        self.edge_mat=[[0 for i in range(self.vertices)] for j in range(self.vertices)]
        
    def add_edge(self,u,v,w):
        self.edge_mat[u][v]=w
#         self.edge_mat[v][u]=w

    def MinDist(self,dist,visited):
        inf=1e10
        for v in range(self.vertices):
            if dist[v]<inf and visited[v]==False:
                inf=dist[v]
                min_idx=v
        return min_idx
        
    def Dijkstra_Algo(self,src):
        inf=1e10
        dist=[inf]*self.vertices
        visited=[False]*self.vertices
        dist[src]=0
        for v in range(self.vertices):
            idx=self.MinDist(dist,visited)
            visited[idx]=True
            for node in range(self.vertices):
                if (self.edge_mat[idx][node]>0 and
                    visited[node]==False and
                    dist[node]>dist[idx]+self.edge_mat[idx][node]):
                        dist[node]=dist[idx]+self.edge_mat[idx][node]
        for node in range(self.vertices):
            print(node ,"\t",":","\t",dist[node])
            
g=Graph(5)
g.add_edge(0,3,3)
g.add_edge(0,2,6)
g.add_edge(1,0,3)
g.add_edge(2,3,1)
g.add_edge(3,2,2)
g.add_edge(3,1,1)
g.add_edge(4,1,4)
g.add_edge(3,4,2)
g.Dijkstra_Algo(0)
