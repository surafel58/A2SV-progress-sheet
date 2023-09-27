class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()
        memo = dict()
        def dp(i, time):

            if i == len(satisfaction):
                return 0
            
            if (i, time) in memo:
                return memo[(i, time)]

            memo[(i, time)] = max((time * satisfaction[i]) + dp(i+1, time + 1), dp(i+1, time))
            return memo[(i, time)]

        return dp(0, 1)
