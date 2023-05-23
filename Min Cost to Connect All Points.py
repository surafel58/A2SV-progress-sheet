class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []
        for i in range(len(points)):
            points[i] = tuple(points[i])


        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                temp = (points[i], points[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))

                edges.append(temp)

        edges.sort(key=lambda a : a[2])
                
        minCost = 0
        unionFind = UnionFind(points)
        countNodes = 0

        for edge in edges:
            a = unionFind.find(edge[0])
            b = unionFind.find(edge[1])

            if a != b:
                if edge[0] == a:
                    countNodes += 1
                if edge[1] == b:
                    countNodes += 1

                unionFind.union(edge[0], edge[1])
                minCost += edge[2]

        return minCost


class UnionFind:
    def __init__(self, points):
        self.root = dict()
        self.size = dict()

        for point in points:

            self.root[point] = point
            self.size[point] = 1

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
