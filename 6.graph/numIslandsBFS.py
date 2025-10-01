from collections import deque

def numIslandsBFS(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    
    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = '0'
        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
    
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                bfs(r, c)
                count += 1
    return count


grid = [
  ["1","1","0","0"],
  ["1","0","0","1"],
  ["0","0","1","1"],
  ["0","0","0","0"]
]

print(numIslandsBFS(grid))
