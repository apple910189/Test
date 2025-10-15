class UnionFind:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.parent = [-1] * (m * n)  # -1 表示水
        self.rank = [0] * (m * n)
        self.count = 0  # 島嶼數量

    def index(self, r, c):
        return r * self.n + c

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        # union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1  # 合併後島嶼數量減 1

class Solution:
    def numIslands2(self, m, n, positions):
        uf = UnionFind(m, n)
        res = []
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        
        for r, c in positions:
            idx = uf.index(r, c)
            if uf.parent[idx] != -1:
                # 重複新增土地，跳過
                res.append(uf.count)
                continue
            uf.parent[idx] = idx  # 新增土地，自己是父節點
            uf.count += 1  # 新增一個島
            # 檢查四個方向
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    n_idx = uf.index(nr, nc)
                    if uf.parent[n_idx] != -1:
                        uf.union(idx, n_idx)
            res.append(uf.count)
        return res

# 範例使用
sol = Solution()
m, n = 3, 3
positions = [[0,0],[0,1],[1,2],[2,1],[1,1]]
print(sol.numIslands2(m, n, positions))
# 輸出: [1,1,2,3,1] （每次操作後的島嶼數量）
