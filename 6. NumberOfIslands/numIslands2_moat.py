class Solution:
    def __init__(self):
        self.parent = []
        self.dx = [0, 0, 1, -1]
        self.dy = [1, -1, 0, 0]
        self.directionCount = 4

    def findParent(self, id):
        if self.parent[id] == id:
            return self.parent[id]
        return self.parent[id] == self.findParent(self.parent[id])

    def union(self, x, y):
        parentX = self.findParent(x)
        parentY = self.findParent(y)
        if parentX != parentY:
            self.parent[parentX] = parentY
            return True
        return False

    def numberOfIslands(self, m, n, positions):
        grid = [[0] * n for _ in range(m)]
        self.parent = [0] * (len(positions) + 1)
        islandsCount = 0
        ans = []

        for i, (x, y) in enumerate(positions):
            id = i + 1
            self.parent[id] = id
            grid[x][y] = id
            islandsCount += 1

            for direction in range(self.directionCount):
                targetX = x + self.dx[direction]
                targetY = y + self.dy[direction]
                if 0 <= targetX < m and 0 <= targetY < n and grid[targetX][targetY] != 0:
                    if self.union(id, grid[targetX][targetY]):
                        islandsCount -= 1
            ans.append(islandsCount)
        return ans

# 範例使用
sol = Solution()
m, n = 3, 3
positions = [[0,0],[0,1],[1,2],[2,1],[1,1]]
print(sol.numberOfIslands(m, n, positions))
# 輸出: [1,1,2,3,1] （每次操作後的島嶼數量）
