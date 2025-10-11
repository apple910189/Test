from collections import deque
from typing import List

class Solution:
    def minimumObstacle(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        directionCount = 4
        
        id_map = [[0] * m for _ in range(n)]
        locationX = [0] * (n * m + 1)
        locationY = [0] * (n * m + 1)
        dis = [-1] * (n * m + 1)
        vis = [0] * (n * m + 1)
        
        index = 0
        for i in range(n):
            for j in range(m):
                index += 1
                id_map[i][j] = index
                dis[index] = -1
                locationX[index] = i
                locationY[index] = j

        q = deque()
        q.append(1) 
        dis[1] = 0
        
        while q:
            currentNode = q.popleft()
            if vis[currentNode]:
                continue
            vis[currentNode] = 1
            
            x = locationX[currentNode]
            y = locationY[currentNode]
            
            for i in range(directionCount):
                targetX = x + dx[i]
                targetY = y + dy[i]
                
                if 0 <= targetX < n and 0 <= targetY < m:
                    newDistance = dis[currentNode]
                    targetId = id_map[targetX][targetY]
                    if grid[targetX][targetY] == 1:
                        newDistance += 1
                    
                    if dis[targetId] == -1 or dis[targetId] > newDistance:
                        dis[targetId] = newDistance
                        if grid[targetX][targetY] == 1:
                            q.append(targetId) 
                        else:
                            q.appendleft(targetId)
        
        return dis[id_map[n - 1][m - 1]]

s = Solution()

grid = [[0,1,1],[1,1,0],[1,1,0]]
ans = s.minimumObstacle(grid)
print(ans)