from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# ---------- DFS (stack 版) ----------
def dfs_stack(graph, start):
    stack = [start]
    visited = set()
    order = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # 注意：為了保持和圖上順序一致，先加入右邊鄰居
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order

# ---------- BFS ----------
def bfs(graph, start):
    queue = deque([start])
    visited = set()
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

print("DFS 訪問順序:", dfs_stack(graph, 'A'))
print("BFS 訪問順序:", bfs(graph, 'A'))
