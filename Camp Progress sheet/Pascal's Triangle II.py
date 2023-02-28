class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
            
        if rowIndex == 1:
            return [1,1]
        
        row = [0] * (rowIndex + 1)
        row[0] = 1
        row[-1] = 1
        
        #get previous row
        prevRow = self.getRow(rowIndex - 1)

        for i in range(1, len(row) - 1):
            row[i] = prevRow[i] + prevRow[i-1]

        return row 


        
