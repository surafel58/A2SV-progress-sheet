class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #0 0 0 0
        #0 1 1 0 
        #1 1 1 0

        zeroRow = set()
        zeroCol = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeroRow.add(i)
                    zeroCol.add(j)

        
        for i in range(m):
            for j in range(n):
                if i in zeroRow or j in zeroCol:
                    matrix[i][j] = 0
