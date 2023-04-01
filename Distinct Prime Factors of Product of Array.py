class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        product = 1

        # for i in range(len(nums)):
            # product *= nums[i]

        primes = set()

        #prime factorization
        for i in range(len(nums)):

            n = nums[i]
            d = 2
            while d * d <= n:
                while n % d == 0:
                    primes.add(d)
                    n //= d
                d += 1

            if n > 1:
                primes.add(n)


        return len(primes)
