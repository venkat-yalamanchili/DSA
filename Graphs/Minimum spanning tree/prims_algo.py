import heapq

def prims_mst_set(V, adj):
    min_heap = [(0, 0)]  # (weight, node)
    visited = set()      # Using a set instead of a list
    mst_weight = 0

    while min_heap and len(visited) < V:
        weight, u = heapq.heappop(min_heap)

        # Check if node is already in the set
        if u in visited:
            continue
        # Add node to the set
        visited.add(u)
        mst_weight += weight

        for neighbor_weight, v in adj[u]:
            if v not in visited:
                heapq.heappush(min_heap, (neighbor_weight, v))

    return mst_weight