class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #1,2,2,3,8
        
        sortedNums = sorted(nums)
        result = []
        sortValue_map = defaultdict(int)

        for i in range(len(nums)):
            sortValue_map[i] = sortedNums.index(nums[i])

        for i in range(len(nums)):
            count = sortValue_map[i]
            result.append(count)

        return result
