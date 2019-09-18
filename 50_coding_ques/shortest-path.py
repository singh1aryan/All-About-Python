"""
shortest path between 2 nodes in a graph
first take - bfs
for path - store parents in a tuple or a dictionary
"""
class Node:
    children = []
    def __init__(self, val):
        self.val=val

    def addChild(self,node):
        self.children.append(node)


def shortestPath(a,b):
    if a==None or b==None: return None # no path exists

    queue = []
    parents = {}
    queue.append(a)
    while len(queue)>0:
        curr = queue.pop(0)
        if curr == b: 
            break # path found
        if curr.children == None: # if doesn't have any children
            continue
        
        for node in curr.children:
            if node in parents:
                queue.append(node) # add to dictionary
                parents[node] = curr # add to parents dict

    if b not in parents: # no path starting from b - bottom up
        print('No path found')
    print(parents)
    path = []
    while b!=None:
        path.append(b)
        b = parents[b]
    return path

"""
classic bfs - queue + visited + parents
"""

graph = []
for i in range(5):
    graph.append(Node(i))

graph[0].addChild(graph[1])
graph[0].addChild(graph[2])
graph[1].addChild(graph[4])
graph[3].addChild(graph[0])
graph[3].addChild(graph[2])
graph[4].addChild(graph[3])
shortestPath(graph[0],graph[3])