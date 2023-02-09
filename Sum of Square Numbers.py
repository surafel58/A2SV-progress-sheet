class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        left = 0
        right = int(sqrt(c))
        while left**2 + right**2 != c and left <= right:
            if left**2 + right**2 > c:
                right -= 1
            else:
                left += 1
        if left > right:
            return False
        return True
