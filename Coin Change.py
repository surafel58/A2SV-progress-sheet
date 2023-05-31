class Solution:
    def __init__(self):
        self.coins = []
        self.memo = dict()
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        minCoins = self.getMinCoins(0, amount)
        
        if minCoins == float('inf'):
            return -1

        return minCoins

    def getMinCoins(self, i, amount):
        
        if amount == 0:
            return 0
        
        if i >= len(self.coins) or amount < 0:
            return float("inf")

        if (i, amount) in self.memo:
            return self.memo[(i, amount)]

        k = min(1 + self.getMinCoins(i, amount - self.coins[i]), self.getMinCoins(i + 1, amount))

        self.memo[(i, amount)] = k

        return k
