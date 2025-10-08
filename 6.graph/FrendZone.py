class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n  # 每個集合的樹高 (rank)
        self.count = n

    def find(self, a):
        # 路徑壓縮
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        print(f'\nunion {x} {y}, [px py] {px} {py}, rank[px py]:{self.rank[px]} {self.rank[py]} ')
        if px == py:
            print("parent:", self.parent)
            print("rank:", self.rank)
            return  # 已經在同一集合

        # 按 rank 合併，保持樹盡量矮
        if self.rank[px] < self.rank[py]:
            print(f'rank[px] < [py], parent[px] = py')
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            print(f'rank[px] > [py], parent[py] = px')
            self.parent[py] = px
        else:
            # 高度相同時，隨便選一個當父節點，並把 rank +1
            self.parent[py] = px
            self.rank[px] += 1
        self.count -= 1
        print("parent:", self.parent)
        print("rank:", self.rank)
        print(f'count:{self.count}')

    def connected(self, x, y):
        # 判斷是否在同一集合
        return self.find(x) == self.find(y)


uf = UnionFind(5)

friends = [
    [1,1,0,0,0],
    [1,1,1,0,0],
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]

for i in range(len(friends)):
    for j in range(len(friends[0])):
        if friends[i][j]==1:
            uf.union(i,j)


