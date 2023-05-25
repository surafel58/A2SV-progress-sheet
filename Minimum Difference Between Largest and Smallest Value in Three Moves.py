class Solution:
    def minDifference(self, nums: List[int]) -> int:
        
        nums.sort()

        #0, 1, 1, 4, 6, 6, 6

        if len(nums) <= 3:
            return 0

        minDiff = float("inf")

        #first option
        temp = nums.copy()

        for i in range(0, 3):
            temp[i] = temp[3]
        
        minDiff = min(minDiff, max(temp) - min(temp))

        #second option
        temp = nums.copy()
        for i in range(-1, -4, -1):
            temp[i] = temp[-4]

        minDiff = min(minDiff, max(temp) - min(temp))

        #third option
        temp = nums.copy()
        temp[0] = temp[1]

        for i in range(-1, -3, -1):
            temp[i] = temp[-3]
        

        minDiff = min(minDiff, max(temp) - min(temp))

        #fourth option
        temp = nums.copy()
        
        temp[-1] = temp[-2]

        for i in range(0, 2):
            temp[i] = temp[2]
        
        
        # temp[0 : 2] = temp[2 : 3]

        minDiff = min(minDiff, max(temp) - min(temp))
        
        return minDiff
