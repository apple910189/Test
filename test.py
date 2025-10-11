from collections import deque
from typing import List
class Solution():
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        dq = deque([(0, 0)])

        while dq:
            x, y = dq.popleft()
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                nx, ny = x+dx, y+dy
                # print(f'xy {x}{y}, dxy {dx} {dy}, nxy {nx} {ny}')
                if 0 <= nx < m and 0 <= ny < n:
                    cost = dist[x][y] + grid[nx][ny]
                    if cost < dist[nx][ny]:
                        print(f'sam1 {cost}')
                        dist[nx][ny] = cost
                        if grid[nx][ny] == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))
        return dist[m-1][n-1]

s = Solution()

grid = [[0,1,1],[1,1,0],[1,1,0]]
ans = s.minimumObstacles(grid)
print(ans)