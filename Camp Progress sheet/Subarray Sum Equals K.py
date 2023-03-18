class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum_freq = defaultdict(int)

        prefixSum = 0
        counter = 0
        prefixSum_freq[0] = 1
        
        for i in range(len(nums)):
            prefixSum += nums[i]
            if prefixSum - k in prefixSum_freq:
                counter += prefixSum_freq[prefixSum - k]
            
            prefixSum_freq[prefixSum] += 1
            
        return counter
