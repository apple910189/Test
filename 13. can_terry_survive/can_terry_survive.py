def can_terry_survive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    m = len(grid)
    n = len(grid[0])
    
    terry_queue = deque()
    fire_queue = deque()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'U':
                terry_queue.append((i, j))
            elif grid[i][j] == 'F':
                fire_queue.append((i, j))
    
    while terry_queue:
        # preemptive check
        for _ in range(len(fire_queue)):
            x, y = fire_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] not in ('*', 'F'):
                    grid[nx][ny] = 'F'
                    fire_queue.append((nx, ny))

        for _ in range(len(terry_queue)):
            x, y = terry_queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] not in ('*', 'U', 'F'):
                    if grid[nx][ny] == 'E':
                        return True
                    grid[nx][ny] = 'U'
                    terry_queue.append((nx, ny))
    
    return False