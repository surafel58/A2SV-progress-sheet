class Solution:
    def countPrimes(self, n: int) -> int:
        #Sieve of erathostenes 

        primes = [True] * n

        if len(primes) < 2:
            return 0

        primes[0], primes[1] = False, False

        i = 2

        while i * i <= n:
            if primes[i]:
                j = i * i
                while j < n:
                    primes[j] = False
                    j += i
            i += 1 

        total = sum(primes)
        return total
