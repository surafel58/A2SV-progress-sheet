class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = 0
        maxSum = float(-inf)
        left = 0
        
        for right in range(len(nums)):
            currentSum += nums[right]

            if right - left + 1 >= k:
                maxSum = max(maxSum, currentSum)
                currentSum -= nums[left]
                left += 1

        result = maxSum / k

        return result
