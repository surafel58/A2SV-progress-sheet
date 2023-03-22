class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1,3,5,7,10,11,16,20,23,30,34,60
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = (m*n)  - 1

        while left <= right:
            mid = left + (right - left) // 2

            value = matrix[mid//n][mid%n]

            if target == value:
                return True
            if target < value:
                right = mid - 1
            else:
                left = mid + 1


        return False 
