class Solution:
    def __init__(self):
        self.memo = dict()

    def uniquePaths(self, m: int, n: int) -> int:
        return self.countPath(m - 1, n - 1)

    def countPath(self, m, n):
        if m == 0 and n == 0:
            return 1
        
        if m < 0 or n < 0:
            return 0

        if (m, n) in self.memo:
            return self.memo[(m, n)]

        k = self.countPath(m - 1, n) + self.countPath(m, n - 1)

        self.memo[(m, n)] = k

        return k
        
