class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        characters = set()
        
        for equation in equations:
            characters.add(equation[0])
            characters.add(equation[-1])
        
        unionFind = UnionFind(characters)

        for equation in equations:
            a = equation[0]
            b = equation[-1]

            if equation[1:3] == "==":
                unionFind.union(a, b)
        
        for equation in equations:
            
            a = equation[0]
            b = equation[-1]
            if equation[1:3] == "!=" and unionFind.find(a) == unionFind.find(b):
                return False

        return True


class UnionFind:
    def __init__(self, initializer):
        
        self.root = dict()
        self.size = dict()

        for char in initializer:
            self.root[char] = char
            self.size[char] = 1


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
        
