class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        return self.findGcd(nums[0], nums[-1])

    def findGcd(self, a, b):
        if b == 0:
            return a
        return self.findGcd(b, a % b)
