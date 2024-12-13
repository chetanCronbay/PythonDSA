class MatrixGraph():
    def __init__(self, size):
        self.size = size # set size of the matrix i.e the number of vertices
        self.matrix = [[0 for _ in range(size)] for _ in range(size)] # make an empty matrix inner loop is [0 for _ in range(size)] and outer loop is [for _ in range(size)] that giver the output like [0][0][0]
                                                               #  [0][0][0]
                                                               #  [0][0][0] with size =3
    
    def addEdge(self, v, u):

        # Add an edge from vertex u to vertex v.
        # By default, the edge weight is 1 (for unweighted graphs).

        self.matrix[u][v] = 1 # added edge from u to  (v -> u)
        self.matrix[v][u] = 1 # as it is an undirected graph there is a two way relation (v -> u)

        # we can also make a directed graph in a same manner by setting self.matrix[v][u] = 0 this will set set a direct edge from only u -> v

    def deleteEdge(self,v,u):
        self.matrix[v][u] = 0 # setting the edge to 0 representing no relation between v and u
        self.matrix[u][v] = 0 # setting the edge to 0 representing no relation between u and v

    def deisplay(self):
        for vertex in self.matrix:
            print(vertex)


#     [a][b][c][d]
#
# [a] [0][1][1][0]
# [b] [1][0][0][1]
# [c] [1][0][0][1]
# [d] [0][1][1][0]

# graph matrix 👆

# A -- B
# |    |
# C -- D

# graph representation 👆

# [0, 1, 1, 0]
# [1, 0, 0, 0]
# [1, 0, 0, 1]
# [0, 0, 1, 0]

# matrix representation after deletion 👆

# A -- B
# |    
# C -- D

# graph representation after deletion 👆


graph = MatrixGraph(4)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,0)
graph.addEdge(1,3)
graph.addEdge(2,0)
graph.addEdge(2,3)
graph.addEdge(3,1)
graph.addEdge(3,2)
graph.deisplay()
print("----------------------------------------------------")
graph.deleteEdge(1,3)
graph.deleteEdge(3,1)
graph.deisplay()