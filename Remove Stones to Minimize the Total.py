class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        #max heap
        heap = [-i for i in piles]
        heapq.heapify(heap)


        for i in range(k):
            temp = -heapq.heappop(heap)
            temp = temp - (temp // 2)
            heapq.heappush(heap, -temp)

        #make it positive
        heap = [-i for i in heap]
        return sum(heap)
