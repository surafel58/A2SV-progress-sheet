class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        visited = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i-j not in visited:
                    visited[i-j] = matrix[i][j]
                elif visited[i-j] != matrix[i][j]:
                    return False
        return True
