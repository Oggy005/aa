def shortest_path(graph, node1, node2):
  path_list = [[node1]]
  path_index = 0

  previous_nodes = {node1}
  if node1 == node2:
     return path_list[0]

  while path_index < len(path_list):
     current_path = path_list[path_index]
     last_node = current_path[-1]
     next_nodes = graph[last_node]

     if node2 in next_nodes:
         current_path.append(node2)
         return current_path

     for next_node in next_nodes:
       if not next_node in previous_nodes:
           new_path = current_path[:]
           new_path.append(next_node)
           path_list.append(new_path)

           previous_nodes.add(next_node)

     path_index += 1

  return []
graph = {}
graph[1] = {2, 5}
graph[2] = {1, 3, 5}
graph[3] = {2, 4}
graph[4] = {3, 5, 6}
graph[5] = {1, 2, 4}
graph[6] = {4}
