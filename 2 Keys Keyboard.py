class Solution:
    def minSteps(self, n: int) -> int:
        
        total = 0

        primeFactors = []

        d = 2

        while d * d <= n:
            while n % d == 0:
                primeFactors.append(d)
                n //= d
            d += 1
        
        if n > 1:
            primeFactors.append(n)

        total = sum(primeFactors)
        return total
        
