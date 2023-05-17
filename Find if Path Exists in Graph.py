class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        unionFind = UnionFind(n)
        for edge in edges:
            unionFind.union(edge[0], edge[1])

        return unionFind.connected(source, destination)



class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size
        
    def representative(self, x):

        x_rep = self.root[x]

        while x_rep != self.root[x_rep]:
            x_rep = self.root[x_rep]
        
        # self.root[x] = self.representative(self.root[x])
        while x != x_rep:
            parent = self.root[x]
            self.root[x] = x_rep
            x = parent
            
        return x_rep
		
    def union(self, x, y):
        x_rep = self.representative(x)
        y_rep = self.representative(y)
        
        if x_rep != y_rep:
            if self.size[x_rep] > self.size[y_rep]:
                self.root[y_rep] = x_rep
                self.size[x_rep] += self.size[y_rep]
                
            else:
                self.root[x_rep] = y_rep
                self.size[y_rep] += self.size[x_rep]        
        
    def connected(self, x, y):
        return self.representative(x) == self.representative(y)
