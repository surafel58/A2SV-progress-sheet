class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):

            num = nums[i] 
            reversed_num = 0

            while num != 0:
                digit = num % 10
                reversed_num = reversed_num * 10 + digit
                num //= 10

            nums.append(reversed_num)
        
        nums = set(nums)

        return len(nums)
