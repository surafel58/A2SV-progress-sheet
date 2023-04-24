class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        x1, x2 = 0, 0
        
        for i in nums:
            x1, x2 = (~i & x1 & ~x2) | (i & ~x1 & x2), ~x1 & (i^x2)
        
        return x2

        
