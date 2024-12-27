# Define the graph as a dictionary where each key is a node and the value is a list of its neighbors
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

# Initialize an empty list to keep track of visited nodes
visited = []

# Define the DFS function that takes the graph, the visited list, and the starting node as arguments
def dfs(graph, visited, node):
    # If the node has not been visited yet
    if node not in visited:
        # Print the node followed by an arrow
        print(f'{node}' " ->", end = " ") # like the first node is 5
        # Add the node to the visited list
        visited.append(node) 
        # Iterate over the neighbors of the current node
        for neighbour in graph[node]: # like the first node is 5 and its neighbours are 3 and 7
            # Recursively call the DFS function for each neighbor
            dfs(graph, visited, neighbour)

# Print the starting message for DFS
print("DFS:")
# Call the DFS function starting from node '5'
dfs(graph, visited, '5')

# Visual representation of the graph:
#     5
#    / \
#   3   7
#  / \   \
# 2   4-- 8

# Output:- DFS: 5 -> 3 -> 2 -> 4 -> 8 -> 7 ->