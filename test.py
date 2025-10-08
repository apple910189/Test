class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n  # 每個集合的樹高 (rank)

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
        print("parent:", self.parent)
        print("rank:", self.rank)

    def connected(self, x, y):
        # 判斷是否在同一集合
        return self.find(x) == self.find(y)

uf = UnionFind(5)
uf.union(0,1)
'''
x=0,y=1
px=0,py=1
rank[0]=1,rank[1]=1
parent[1]=0
rank[0]+1
parent = [0,0,2,3,4]
rank = [2,1,1,1,1]
'''

uf.union(2,3)
'''
x=2,y=3
px=2,px=3
rank[2]=1,rank[3]=1
parent[3]=2
rank[2]+=1
parent = [0,0,2,2,4]
rank = [2,1,2,1,1]

'''

uf.union(1,2)
'''
x=1,x=2
px=0,py=2
rank[px]=2,rank[py]=2
parent[py=2] = px=0
rank[px=0] += 1
parent=[0,0,0,2,4]
rank = [3,1,2,1,1]
'''
