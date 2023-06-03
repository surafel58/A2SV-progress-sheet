class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = dict()

        def dp(row_index, col_index):
            
            if row_index >= len(triangle):
                return 0

            if (row_index, col_index) in memo:
                return memo[(row_index, col_index)]

            leftChoice = triangle[row_index][col_index] + dp(row_index + 1, col_index)
            rightChoice = triangle[row_index][col_index + 1] + dp(row_index + 1, col_index + 1)

            memo[(row_index, col_index)] = min(leftChoice, rightChoice) 

            return memo[(row_index, col_index)]


        return triangle[0][0] + dp(1, 0) 

 
