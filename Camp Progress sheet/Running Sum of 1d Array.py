class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = nums
        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + nums[i]

        return prefixSum
