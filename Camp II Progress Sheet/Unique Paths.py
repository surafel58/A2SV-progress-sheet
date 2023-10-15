class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if n == 1 or m == 1:
            return 1
            
        n = max(m, n) - 1 + min(m, n) - 1
        r = min(m, n) - 1

        
        return int(math.factorial(n) / (math.factorial(r) * (math.factorial(n - r))))
