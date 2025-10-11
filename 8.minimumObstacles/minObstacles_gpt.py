from collections import deque
from typing import List
class Solution():
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])                  # 取出m n
        dist = [[float('inf')] * n for _ in range(m)]   # 創建dist 全部放 inf
        dist[0][0] = 0                                  # 初始化 dist[0][0]
        dq = deque([(0, 0)])                            # 初始化 dq

        while dq:                                       # 如果 dq 有值
            x, y = dq.popleft()                         # dq pop 左邊得到x y
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:  # for迴圈四種情形
                nx, ny = x+dx, y+dy                     # 計算 x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n:         # 如果 x+dx 大於 0且小於m, y+dy 大於 0且小於n (表示在grid內)
                    cost = dist[x][y] + grid[nx][ny]    # 計算當前 xy 的 cost
                    if cost < dist[nx][ny]:             # 如果 cost 小於當前xy也就是 dist[nx][ny]
                        dist[nx][ny] = cost             # 更新 xy 的 cost
                        if grid[nx][ny] == 0:           # 如果 grid xy 是0
                            dq.appendleft((nx, ny))     # dq 加左邊
                        else:
                            dq.append((nx, ny))         # dq 加右邊
        return dist[m-1][n-1]                           # 返回最後一個

s = Solution()

grid = [[0,1,1],[1,1,0],[1,1,0]]
ans = s.minimumObstacles(grid)
print(ans)