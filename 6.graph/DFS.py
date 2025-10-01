graph = {
    'A': ['B'],
    'B': ['A', 'C'],
    'C': ['B']
}

stack = ['A']        # 從 A 出發
visited = set()      # 記錄已經訪問過的節點
order = []           # 存放訪問順序



while stack:
    print(f'stack:{stack}')
    node = stack.pop()        # 從 stack 取出最後加入的節點（後進先出）
    if node not in visited:   # 如果還沒訪問過
        visited.add(node)     
        order.append(node)
        # 把沒訪問過的鄰居加入 stack
        for neighbor in graph[node]:
            if neighbor not in visited:
                print(f'push neighbor to stack:{neighbor}')
                stack.append(neighbor)

print("DFS 訪問順序:", order)
