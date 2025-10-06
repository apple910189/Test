class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n  # 每個集合的樹高 (rank)

    def find(self, a):
        # 路徑壓縮
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px == py:
            return  # 已經在同一集合

        # 按 rank 合併，保持樹盡量矮
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            # 高度相同時，隨便選一個當父節點，並把 rank +1
            self.parent[py] = px
            self.rank[px] += 1

    def connected(self, x, y):
        # 判斷是否在同一集合
        return self.find(x) == self.find(y)


uf = UnionFind(5)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print("parent:", uf.parent)
print("rank:", uf.rank)
print("connected(0,2):", uf.connected(0,2))  # True
print("connected(0,3):", uf.connected(0,3))  # False

