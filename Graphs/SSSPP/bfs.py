from collections import deque

class Graph:
    def __init__(self, gdict=None):
        self.gdict = gdict if gdict else {}

    def bfs(self, start, end):
        queue = deque([[start]])
        visited = {start}
        
        while queue:
            path = queue.popleft()
            node = path[-1]
            
            if node == end:
                return path
            
            for adjacent in self.gdict.get(node, []):
                if adjacent not in visited:
                    visited.add(adjacent)
                    queue.append(path + [adjacent])
        return None

graph_data = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}

g = Graph(graph_data)
print(g.bfs('A', 'G'))