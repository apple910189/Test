from collections import deque

graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

queue = deque(['A'])   # BFS 用 queue
visited = set()
order = []

while queue:
    node = queue.popleft()   # 先進先出
    if node not in visited:
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

print("BFS 訪問順序:", order)
