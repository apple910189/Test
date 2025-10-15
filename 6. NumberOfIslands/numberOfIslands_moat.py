class Solution:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        self.directionCount = 4

    def dfs(self, x, y, grid):
        grid[x][y] = 0
        for i in range(self.directionCount):
            targetX = x + self.dx[i]
            targetY = y + self.dy[i]
            if 0 <= targetX < self.n and 0 <= targetY < self.m and grid[targetX][targetY] == 1:
                self.dfs(targetX, targetY, grid)

    def numberOfIslands(self, grid):
        self.n = len(grid)
        if self.n == 0:
            return 0
        self.m = len(grid[0])
        ans = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == 1:
                    self.dfs(i, j, grid)
                    ans += 1
        return ans