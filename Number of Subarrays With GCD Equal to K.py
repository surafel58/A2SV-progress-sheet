class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:

        def findGcf(a, b):
            if b == 0:
                return a
            return findGcf(b, a % b)

        count = 0

        for i in range(len(nums)):
            gcf = nums[i]

            for j in range(i, len(nums)):
                gcf = findGcf(gcf, nums[j])
                
                if gcf == k:
                    count += 1

        return count
