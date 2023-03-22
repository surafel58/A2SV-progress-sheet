class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #1,3,5,7,10,11,16,20,23,30,34,60
        m = len(matrix)
        n = len(matrix[0])
        searchSpace = []

        for i in range(m):
            for j in range(n):
                searchSpace.append(matrix[i][j])

        targetIndex = bisect_left(searchSpace, target)

        if targetIndex < (m*n) and target == searchSpace[targetIndex]:
            return True
        return False 
