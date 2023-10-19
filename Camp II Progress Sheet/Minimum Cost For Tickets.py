class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        allDays = [[i, False] for i in range(0, 366)]
        for i in range(len(days)):
            j = days[i]
            allDays[j][1] = True

        memo = dict()

        def dp(day):

            if day > days[-1]:
                return 0

            if day in memo:
                return memo[day]

            if allDays[day][1]:
                memo[day] = min(costs[0] + dp(day + 1), costs[1] + dp(day + 7), costs[2] + dp(day + 30))
            else:
                memo[day] = dp(day + 1)

            return memo[day]

        return dp(0)
