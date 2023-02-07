class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        limit = len(piles) // 3
        
        counter = 0
        i = len(piles) - 2
        max = 0
        while counter < limit:
            max += piles[i]
            i -= 2
            counter += 1
        return max

