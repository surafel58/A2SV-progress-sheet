class Solution:
    def __init__(self):
        self.visited = set()

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(n):
                if (i,j) in self.visited:
                    continue
                    
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp


                self.visited.add((i,j))
                self.visited.add((n-1-j,i))
                self.visited.add((n-1-i,n-1-j))
                self.visited.add((j,n-1-i))
