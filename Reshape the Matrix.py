class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        if (r * c) != (col * row):
            return mat
        
        temp = []
        result = []
        for i in range(row):
            for j in range(col):
                temp.append(mat[i][j])
        
        tempIndex = 0
        for i in range(r):
            rowValues = []
            for j in range(c):
                rowValues.append(temp[tempIndex])
                tempIndex += 1
            result.append(rowValues)

        return result
