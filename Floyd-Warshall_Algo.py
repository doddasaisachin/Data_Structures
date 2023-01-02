class Graph(object):
    def __init__(self,vertices):
        self.vertices=vertices
        self.init_mat=[[0 for i in range(self.vertices)] for j in range(self.vertices)]
    def add_edge(self,u,v,w):
        self.init_mat[u][v]=w
    def floyd_warshall(self):
        init_mat=self.init_mat
        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    init_mat[i][j]=min(init_mat[i][j],init_mat[i][k]+init_mat[k][j])
        return self.print_solution(init_mat)
    def print_solution(self,mat):
        for lis in mat:
            for ele in lis:
                print(ele," ",end="")
            print()        
        
g=Graph(4)
g.add_edge(0,1,3)
g.add_edge(0,2,9999)
g.add_edge(0,3,5)
g.add_edge(1,0,2)
g.add_edge(1,2,9999)
g.add_edge(1,3,4)
g.add_edge(2,0,9999)
g.add_edge(2,1,1)
g.add_edge(2,3,9999)
g.add_edge(3,0,9999)
g.add_edge(3,1,9999)
g.add_edge(3,2,2)
g.floyd_warshall()
