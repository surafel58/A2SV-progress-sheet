class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rowSize = len(self.matrix)
        self.colSize = len(self.matrix[0])

        #prefix sum 
        for i in range(self.rowSize):
            for j in range(1, self.colSize):
                
                self.matrix[i][j] += self.matrix[i][j-1]
        #prefix column sum
        for i in range(self.colSize):
            for j in range(1, self.rowSize):
                self.matrix[j][i] += self.matrix[j-1][i]

        self.matrix.append([0] * self.colSize)
        
        for i in range(self.rowSize):
            self.matrix[i].append(0)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = (self.matrix[row2][col2] - self.matrix[row1-1][col2]) - (self.matrix[row2][col1-1] - self.matrix[row1-1][col1-1])
        return result 
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
