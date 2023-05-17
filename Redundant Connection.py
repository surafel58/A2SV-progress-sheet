class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))

        for edge in edges:

            result = unionFind.union(edge[0] - 1, edge[1] - 1)
            if result:
                return result
        
        return None

class UnionFind:
    def __init__(self, size):
        
        self.root = [i for i in range(size)]
        self.size = [1 for i in range(size)]
        self.solution = None

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

        if x_rep == y_rep:
            
            # self.solution = [x + 1, y + 1]
            return [x + 1, y + 1]
        
        else:
            if self.size[x_rep] > self.size[y_rep]:
                self.root[y_rep] = self.root[x_rep]
                self.size[x_rep] += self.root[y_rep]

            else:
                self.root[x_rep] = self.root[y_rep]
                self.size[y_rep] += self.root[x_rep]

