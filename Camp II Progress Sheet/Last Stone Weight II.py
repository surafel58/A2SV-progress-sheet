class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        totalSum = sum(stones)
        target = ceil(totalSum / 2)
        memo = dict()

        def dp(i, total):

            if total >= target or i == len(stones):
                return abs(total - (totalSum - total))

            if (i, total) in memo:
                return memo[(i, total)]
            
            memo[(i, total)] = min(dp(i + 1, total), dp(i + 1, total + stones[i]))
            return memo[(i, total)]

        return dp(0, 0)
