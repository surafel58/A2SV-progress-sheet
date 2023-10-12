class Solution:
    def countOrders(self, n: int) -> int:
        
        def countAll(n):

            if n == 1:
                return 1

            prev = countAll(n - 1)
            idx = 2 * (n - 1) + 1
            premute = prev * (idx*(idx+1) // 2)
            return premute % (10**9 + 7)

        return countAll(n)
