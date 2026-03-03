import heapq

def shortest_path(adj, src):
    result = {} 
    minheap = [[0, src]]

    while minheap:
        w1, n1 = heapq.heappop(minheap)
        if n1 in result:
            continue
        result[n1] = w1

        for n2, w2 in adj[n1]:
            if n2 not in result:
                heapq.heappush(minheap, [w1 + w2, n2])

    for i in adj.keys():
        if i not in result:
            result[i] = -1
    return result

# --- Test Data ---
# Imagine a triangle: A -> B (2), B -> C (1), A -> C (5)
# The shortest path A to C should be A -> B -> C (Total 3)
graph = {
    'A': [['B', 2], ['C', 5]],
    'B': [['C', 1]],
    'C': [],
    'D': [] # Isolated node to test the -1 logic
}

# Run the test
print(f"Shortest paths from A: {shortest_path(graph, 'A')}")