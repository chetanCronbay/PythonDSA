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

# Initialize an empty list to use as a queue for BFS
queue = []

# Define the BFS function that takes the graph, the visited list, and the starting node as arguments
def bfs(graph, visited, node):
    # Add the starting node to the visited list
    visited.append(node)
    # Add the starting node to the queue
    queue.append(node)

    # While the queue is not empty
    while queue:
        # Remove the first element from the queue
        m = queue.pop(0)
        # Print the node followed by an arrow
        print(f'{m}' " ->", end = " ")

        # Iterate over the neighbors of the current node
        for neighbour in graph[m]:
            # If the neighbor has not been visited yet
            if neighbour not in visited:
                # Add the neighbor to the visited list
                visited.append(neighbour)
                # Add the neighbor to the queue
                queue.append(neighbour)
    print("end")

# Print the starting message for BFS
print("BFS:")
# Call the BFS function starting from node '5'
bfs(graph, visited, '5')

# Visual representation of the graph:
#     5
#    / \
#   3   7
#  / \   \
# 2   4---8

# Output: BFS: 5 -> 3 -> 7 -> 2 -> 4 -> 8 -> end