class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = dict()

        def dp(i):
            if i >= len(questions):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(questions[i][0] + dp(i + questions[i][1] + 1), dp(i + 1))

            return memo[i]

        return dp(0)
