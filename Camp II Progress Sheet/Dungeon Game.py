class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
         
        memo = dict()
        inBound = lambda r, c : -1 < r < len(dungeon) and -1 < c < len(dungeon[0])

        def dp(row, col, hp):

            if not inBound(row, col) or hp <= 0:
                return False

            if (row, col) == (len(dungeon) - 1, len(dungeon[0]) - 1) and (hp + dungeon[row][col]) > 0:
                return True

            if (row, col, hp) in memo:
                return memo[(row, col, hp)]

            memo[(row, col, hp)] = dp(row, col + 1, hp + dungeon[row][col]) or  dp(row + 1, col, hp + dungeon[row][col])

            return memo[(row, col, hp)]

        left = 1
        right = 100000

        while left < right:

            mid = left + (right - left) // 2 

            if dp(0, 0, mid):
                right = mid

            else:
                left = mid + 1

        return right
