# An adjacency list uses a dictionary or a list of lists to store edges for each vertex. This is a space-efficient way to represent sparse graphs.

class ListGraph():
    def __init__(self):
        self.graph = {} # create an empty graph to store the relation between virtices

    def addEdge(self, u, v): # u and v are vertices
        if u not in self.graph:
            self.graph[u] = [] # make empty vertex if u vertex is not present
        
        if v not in self.graph:
            self.graph[v] = [] # make empty vertex if v vertex is not present

        self.graph[u].append(v) # add edge from u to v ( u - v )
        self.graph[v].append(u) # add edge from v to u ( v - u ) in case of undirectional graph in case of directional graph no need to add this line

    def delEdge(self, u, v):
        # Check if u exists in the graph
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)  # Remove edge from u to v

        # Check if v exists in the graph
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)  # Remove edge from v to u (for undirected graph)

    def display(self):
        for vertex, edge in self.graph.items(): 
            print(f'{vertex} -> {edge}')
        
        # The .items() method of a dictionary returns all its key-value pairs as tuples.
        # For example, if self.graph = {0: [1], 1: [0, 2], 2: [1, 3]}, then self.graph.items() will return:
        # [(0, [1]), (1, [0, 2]), (2, [1, 3])]

graph = ListGraph()
graph.addEdge('A','B')
graph.addEdge('B','D')
graph.addEdge('A','C')
graph.addEdge('C','D')
graph.display()

# A -> ['B', 'C']
# B -> ['A', 'D']
# D -> ['B', 'C']
# C -> ['A', 'D']

# list representation 👆

# A -- B
# |    |
# C -- D

# graph representation 👆

print("----------------------------------------------------")
graph.delEdge('B','D')
graph.display()

# A -> ['B', 'C']
# B -> ['A']
# D -> ['C']
# C -> ['A', 'D']

# list representation after deletion 👆

# A -- B
# |    
# C -- D

# graph representation after deletion 👆
