class Solution:
    def knightDialer(self, n: int) -> int:
        
        directions = [[-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [1, 2], [-1, -2], [1, -2]]
        inBound = lambda r, c : -1 < r < 4 and -1 < c < 3
        grid = [[1,2,3], [4,5,6], [7,8,9], [-1,0,-1]]
        result = 0
        memo = dict()
        mod = 10**9 + 7

        def dp(n, r, c):

            if n == 1:
                return 1

            if (n, r, c) in memo:
                return memo[(n, r, c)]

            res = 0
            for direction in directions:
                new_row = r + direction[0]
                new_col = c + direction[1]

                if inBound(new_row, new_col) and grid[new_row][new_col] != -1:
                    res += dp(n - 1, new_row, new_col)

            memo[(n, r, c)] = res
            return memo[(n, r, c)]

        for i in range(4):
            for j in range(3):
                if grid[i][j] != -1:
                    result += dp(n, i, j)

        return result % mod
