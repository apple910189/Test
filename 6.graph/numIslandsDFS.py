
def numIslandsDFS(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    print(f'rows:{rows} cols:{cols}')
    
    def dfs(r, c, index='start'):
        print(f'{index}')
        # if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
        #     return
        print(f'[{r},{c}]')
        if r < 0:
            print('r < 0, return')
            return
        elif r >= rows:
            print('r >= rows, return')
            return
        elif c < 0:
            print('c < 0, return')
            return
        elif c >= cols:
            print('c >= cols, return')
            return
        elif grid[r][c] == '0':   # 注意這裡是字串 '0'
            print('grid[r][c] == 0, return')
            return
        
        grid[r][c] = '0'  # 標記已訪問
        dfs(r+1, c, 'r+1')
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
grid = [
  ["1","0","0"],
  ["0","0","1"],
  ["0","0","1"],
]

print(numIslandsDFS(grid))
