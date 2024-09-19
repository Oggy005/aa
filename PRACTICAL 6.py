def print_adjacency_matrix(vertices, edges):
   adj_matrix = [[0 for _ in range(vertices)] for _ in range(vertices)]


   for edge in edges:
     u, v = edge
     adj_matrix[u][v] = 1
     adj_matrix[v][u] = 1 # If the graph is undirected


   for row in adj_matrix:
    print(" ".join(map(str, row)))


vertices = 5
edges = [(0, 1), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (3, 4)]

print("Adjacency Matrix:")
print_adjacency_matrix(vertices, edges)
