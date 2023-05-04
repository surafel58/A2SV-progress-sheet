class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-i for i in stones]

        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = -heapq.heappop(stones)
            stone2 = -heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, -(stone1 - stone2))

        if len(stones) == 1:
            return -stones[0]
            
        return 0

        
        
