# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        badVersion = -1

        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            temp = isBadVersion(mid)

            if temp:
                badVersion = mid
                right = mid - 1
            else:
                left = mid + 1
                

        return badVersion
