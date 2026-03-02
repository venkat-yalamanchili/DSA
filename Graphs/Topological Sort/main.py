from collections import defaultdict

class Graph:
    def __init__(self):
        # We use a dictionary where each key is a node 
        # and the value is a list of its neighbors.
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topo_help(self, v, visited, stack):
        visited.add(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if i not in visited:
                self.topo_help(i, visited, stack)

        # "Post-order": Push to stack AFTER neighbors are done
        stack.append(v)

    def topologicalsort(self):
        visited = set()
        stack = []

        # We must check every node in the graph
        for k in list(self.graph):
            if k not in visited:
                self.topo_help(k, visited, stack)
            
        print("Topological Sort Order:", stack[::-1])

# --- Let's test it! ---
g = Graph()
g.add_edge("Socks", "Shoes")
g.add_edge("Pants", "Shoes")
g.add_edge("Shirt", "Belt")
g.add_edge("Pants", "Belt")

g.topologicalsort()