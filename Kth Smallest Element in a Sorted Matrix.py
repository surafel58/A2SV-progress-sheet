class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        n  = len(matrix)
        result = 0

        for i in range(n):
            temp = matrix[i]
            heapq.heapify(temp)
        
        heapq.heapify(matrix)
        
        i = 0
        while i < k:
            arr = heapq.heappop(matrix)
            
            if len(arr) != 0:            
                result = heapq.heappop(arr)
                heapq.heappush(matrix, arr)
                i += 1

        return result
