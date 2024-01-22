from Task_1 import kharkiv_metro_graph
import networkx as nx
from collections import deque

def dfs_iterative(graph, start_vertex):
    visited = []
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()  
        if vertex not in visited:    
            visited.append(vertex)
            neighbors = list(graph[vertex])
            stack.extend(reversed(neighbors)) 

    return visited


def bfs_iterative(graph, start):
    visited = []
    queue = deque([start])

    while queue:  
        vertex = queue.popleft()

        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(graph[vertex]) - set(visited))

    return visited  

graph = kharkiv_metro_graph()
adjacency_list = nx.to_dict_of_lists(graph)

print(f"\nDFS: {dfs_iterative(adjacency_list, 'Metrobudivnykiv')}")
print(f"\nBFS: {bfs_iterative(adjacency_list, 'Metrobudivnykiv')}\n") 

