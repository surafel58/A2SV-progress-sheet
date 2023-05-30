class Solution:
    def __init__(self):
        self.memo = dict()
        self.memo[0] = 0
        self.memo[1] = 1
        self.memo[2] = 1

    def tribonacci(self, n: int) -> int:
        if n <= 2 or n in self.memo:
            return self.memo[n]

        k = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        self.memo[n] = k

        return k  
        
