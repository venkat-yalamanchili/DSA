from collections import deque

graph = {

}

def bfs(vertex):
    visited = set()
    visited.add(vertex)
    queue = deque([vertex])
    while queue:
        current = queue.popleft()
        print(current)
        for adjacent in graph[current]:
            if adjacent not in visited:
                visited.add(adjacent)
                queue.append(adjacent)
