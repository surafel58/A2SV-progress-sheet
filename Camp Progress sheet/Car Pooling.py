class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        maxPosition = max(trips, key = lambda a : a[2])
        minPosition = min(trips, key = lambda a : a[0])
        
        positions = [0] * (maxPosition[2] + 1)
        n = len(trips)
        m = len(positions)

        for i in range(n):
            positions[trips[i][1]] += trips[i][0] 
            positions[trips[i][2]] -= trips[i][0]

        for i in range(m):
            if i > 0:
                positions[i] += positions[i-1]

            if positions[i] > capacity:
                return False

        return True

         

        
