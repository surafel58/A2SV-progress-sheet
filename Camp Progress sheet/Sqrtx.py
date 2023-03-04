class Solution:
    def mySqrt(self, x: int) -> int:

        left = 1
        right = x // 2
        target = 0
        while left <= right:
            mid = left + (right - left) // 2

            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                target = mid
                left = mid + 1

        return target
