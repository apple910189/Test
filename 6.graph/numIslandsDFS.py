from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'  # 標記已訪問
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count

grid2 = [
  ["1","1","1","1"],
  ["1","1","1","1"],
  ["1","1","1","1"],
  ["1","1","1","1"]
]

grid1 = [
  ["1","1"],
  ["1","1"]
]
grid = [
  ["1","0","0"],
  ["0","0","1"],
  ["0","0","1"],
]

grid3 = []
s = Solution()
print(s.numIslands(grid))











