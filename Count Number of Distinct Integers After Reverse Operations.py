class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            temp = str(nums[i])
            temp = temp[::-1]

            nums.append(int(temp))

        nums = set(nums)

        return len(nums)
