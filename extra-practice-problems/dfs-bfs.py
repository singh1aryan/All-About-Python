def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    print(visited)
    return visited

def bfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    print(visited)
    return visited

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}
bfs(graph, 'A')