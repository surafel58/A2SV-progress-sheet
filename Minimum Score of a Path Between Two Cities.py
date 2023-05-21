class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        unionFind = UnionFind(n)
        minScore = float('inf')

        for road in roads:
            unionFind.union(road[0], road[1])

        for road in roads:
            if unionFind.find(road[0]) == unionFind.find(1):
                minScore = min(minScore, road[2])
             
        return minScore

class UnionFind:
    def __init__(self, n):
        
        self.root = dict()
        self.size = dict()

        for i in range(1, n + 1):
            self.root[i] = i
            self.size[i] = 1

    def find(self, x):
        
        root = self.root[x]

        while root != self.root[root]:
            root = self.root[root]

        while x != root:
            parent = self.root[x]
            self.root[x] = root
            x = parent
        
        return root
    
    def union(self, x, y):
        
        x_rep = self.find(x)
        y_rep = self.find(y)

        if x_rep != y_rep:
            if self.size[x_rep] > self.size[y_rep]:

                self.root[y_rep] = self.root[x_rep]
                self.size[x_rep] += self.size[y_rep]

            else:
                self.root[x_rep] = self.root[y_rep]
                self.size[y_rep] += self.size[x_rep]
