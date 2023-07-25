class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = dict()
        n = len(matrix[0])
        result = float('inf')

        def findMinSum(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            
            if col < 0 or col >= n:
                return float('inf')

            if row == (n - 1):
                return matrix[row][col]
            
            memo[(row, col)] = matrix[row][col] + \
            min(findMinSum(row + 1, col - 1), findMinSum(row + 1, col), findMinSum(row + 1, col + 1))

            return memo[(row, col)]

        for j in range(n):
            result = min(result, findMinSum(0, j))

        return result
