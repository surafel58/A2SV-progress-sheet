class Solution:
    def __init__(self):
        self.memo = dict()
        self.cost = []

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.cost.append(0)

        return self.minCost(len(cost) - 1)

    def minCost(self, n):
        if n <= 1:
            return self.cost[n]

        if n in self.memo:
            return self.memo[n]

        k = self.cost[n] + min(self.minCost(n - 1), self.minCost(n - 2))

        self.memo[n] = k

        return k
