def bellmanford(V, edges, src):
    result = [float("inf")] * V
    result[src] = 0

    for i in range(V):
        for u,v,wt in edges:
            if result[u] != float("inf") and result[u] + wt < result[v]:
                if i == V-1:
                    return -1
                result[v] = result[u] + wt
    return result


if __name__ == '__main__':
    V = 5
    edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
    src = 0
    
    print(bellmanford(V, edges, src))