from collections import deque
from typing import List
class Solution():
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])                  # 取出m n
        dist = [[float('inf')] * n for _ in range(m)]   # 創建dist 全部放 inf
        dist[0][0] = 0                                  # 初始化 dist[0][0]
        dq = deque([(0, 0)])                            # 初始化 dq
        print(f'初始ＤＱ {dq}')
        while dq:                                       # 如果 dq 有值
            print(f'\nＤＱ取左 {dq}')
            x, y = dq.popleft()                         # dq pop 左邊得到x y
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:  # for迴圈四種方向dx dy
                nx, ny = x+dx, y+dy                     # x y 移動到 nx ny
                print('> > > > > >')
                print(f'面板起點 x: {x} y: {y}')
                print(f'取一方向 dx:{dx} dy:{dy}')
                print(f'算出終點 nx:{nx} ny:{ny}')
                if 0 <= nx < m and 0 <= ny < n:         # 檢查移動後 nx ny是否在grid內
                    cost = dist[x][y] + grid[nx][ny]    # 利用 dist[x][y] + grid[nx][ny] 計算cost
                    print(f'計板成本 dist[{x}][{y}]:{dist[x][y]}')
                    print(f'面板成本 grid[{nx}][{ny}]:{grid[nx][ny]}')
                    print(f'移動成本 cost:{cost}')
                    if cost < dist[nx][ny]:             # 如果 cost 小於當前xy也就是 dist[nx][ny]
                        print(f'移動成本:{cost} 小於 計板成本:{dist[nx][ny]}，進行更新')
                        dist[nx][ny] = cost             # 更新 xy 的 cost
                        print(f'更新計板 dist[{nx}][{ny}]:{dist[nx][ny]}')
                        if grid[nx][ny] == 0:           # 如果 grid xy 是0
                            dq.appendleft((nx, ny))     # dq 加左邊
                            print(f'grid[{nx}][{ny}]== {grid[nx][ny]} ＤＱ加左 {dq}')
                        else:
                            dq.append((nx, ny))         # dq 加右邊
                            print(f'grid[{nx}][{ny}]== {grid[nx][ny]} ＤＱ加右 {dq}')
                    else:
                        print(f'移動成本:{cost} 大於等於 計板成本:{dist[nx][ny]}，不用更新')
        return dist[m-1][n-1]                           # 返回最後一個

s = Solution()

grid = [[0,1,1],[1,1,0],[1,1,0]]
ans = s.minimumObstacles(grid)
print(ans)