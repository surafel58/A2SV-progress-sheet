class Solution:
    def minSteps(self, n: int) -> int:
        
        memo = dict()
        def dp(n, curr, copied):
            if n == 0:
                return 0
                
            if n < 0:
                return (2**31 - 1)

            if (n, curr, copied) in memo:
                return memo[(n, curr, copied)]

            ans1 = (2**31 - 1)
            ans2 = (2**31 - 1)

            ans1 = 1 + dp(n - copied, curr + copied, copied)
            
            if curr != copied:
                ans2 = 1 + dp(n, curr, curr)

            memo[(n, curr, copied)] = min(ans1, ans2)

            return memo[(n, curr, copied)] 

        if n == 1:
            return 0

        return 1 + dp(n - 1, 1, 1)
