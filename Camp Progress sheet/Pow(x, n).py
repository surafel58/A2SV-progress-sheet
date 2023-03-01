class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1

        if n < 0:
            return  1 / self.myPow(x, abs(n))

        return self.myPow(x * x, abs(n // 2)) if n % 2 == 0 else x * self.myPow(x, abs(n -1))
    
