

class Solution:
    def __init__(self):
        self.count = 0

    def numIslandsDFS(self,grid):
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, step=''):
            self.count+=1
            print(f'count {self.count} step:{step} r: {r} c: {c}')
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                print(f' return')
                return
            grid[r][c] = '0'
            dfs(r+1, c, 'r+1')  # 1,0 2,0
            dfs(r-1, c, 'r-1')
            dfs(r, c+1, 'c+1')
            dfs(r, c-1, 'c-1')
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
grid3 = [
  ["1"],
  ["1"],
]
grid = [
  ["1","0","0"],
  ["0","0","1"],
  ["0","0","1"],
]

s = Solution()
print(s.numIslandsDFS(grid3))




'''
r=0,c=0
g[0,0]=1
g[0,0]=0

r=1,c=0
g[1,0]=1
g[1,0]=0

r=2,c=0
return

'''










