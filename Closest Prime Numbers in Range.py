class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        n = right
        primes = [True for i in range(n + 1)]

        primes[0],primes[1] = False, False

        i = 2
        while i * i <= n:
            
            if primes[i]:
                j = i * i
                while j <= n:
                    primes[j] = False
                    j += i
            i += 1

        prev = -1
        minValue = float('inf')
        result = []
        
        for i in range(right, left - 1, -1):
            
            if prev == -1 and primes[i]:
                prev = i

            elif primes[i] and prev != -1:
                
                if prev - i <= minValue:
                    minValue = (prev - i)
                    result = [i, prev]
                
                prev = i

        if len(result) == 0:
            result = [-1, -1]
        
        return result
