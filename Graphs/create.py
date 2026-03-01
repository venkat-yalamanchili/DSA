class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addVertex(self,vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []
            return True
        return False

    def addEdge(self,vertex1,vertex2):
        if vertex1 in self.gdict and vertex2 in self.gdict:
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self,vertex1,vertex2):
        if vertex1 in self.gdict and vertex2 in self.gdict:
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False 
    
    def remove_vertex(self,vertex):
        if vertex in self.gdict:
            for other_vertex in self.gdict[vertex]:
                self.gdict[other_vertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
      
cust_di = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}


graph = Graph(cust_di)
print(graph.gdict)
graph.addEdge("D","A")
print(graph.gdict)