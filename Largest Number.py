class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def keyfunc(a, b):
            a = str(a)
            b = str(b)
            if (a+b) > (b+a):
                return 1
            elif b+a > a+b:
                return -1
            else:
                return 0
        
        nums = sorted(nums, cmp = keyfunc, reverse=True)

        nums = list(map(str, nums))
        result = "".join(nums)
        if result[0] == "0":
            return "0"
        
        return result
        
