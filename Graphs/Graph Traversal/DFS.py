graph = {
    
}

def dfs(vertex):
    visited = set()
    visited.add(vertex)
    stack = [vertex]
    while stack:
        current = stack.pop()
        print(current)
        for adjacent in graph[current]:
            if adjacent not in visited:
                visited.add(adjacent)
                stack.append(adjacent)