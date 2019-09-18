#   A -> B
#   A -> C
#   B -> C
#   B -> D
#   C -> D
#   D -> C
#   E -> F
#   F -> C

"""
path - 
shortest path - 
all paths - 
"""
from collections import deque
from collections import defaultdict 

graph = {'A': ['B', 'C'],
            'B': ['C', 'D'],
            'C': ['D'],
            'D': ['C'],
            'E': ['F'],
            'F': ['C']}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest
    
def bfs_shortest(graph, start, end):
    dist = {start: [start]}
    q = deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = [dist[at], next]
                q.append(next)
    return dist[end]

  

# function for adding edge to graph 
graph1 = defaultdict(list) 
def addEdge(graph,u,v): 
    graph1[u].append(v) 
  
# definition of function 
def generate_edges(graph1): 
    edges = [] 
    # for each node in graph 
    for node in graph1: 
          
        # for each neighbour node of a single node 
        for neighbour in graph1[node]: 
              
            # if edge exists then append 
            edges.append((node, neighbour)) 
    return edges 

graph1 = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }
addEdge(graph,'a','c') 
addEdge(graph,'b','c') 
addEdge(graph,'b','e') 
addEdge(graph,'c','d') 
addEdge(graph,'c','e') 
addEdge(graph,'c','a') 
addEdge(graph,'c','b') 
addEdge(graph,'e','b') 
addEdge(graph,'d','c') 
addEdge(graph,'e','c') 
print(generate_edges(graph1))
print(find_path(graph, 'A', 'D'))
print(bfs_shortest(graph, 'A', 'D'))
# print(find_all_paths(graph, 'A', 'D'))