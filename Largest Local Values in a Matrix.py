class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        localMaxList = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid[0])):
                localmax = self.getlocalMax(grid, i, j, localMaxList)
                if localmax != -1:
                    temp.append(localmax)
            
            if len(temp) != 0:
                localMaxList.append(temp)

        return localMaxList

                        
    def getlocalMax(self, grid, i, j, localMaxList):
        if (i+2) >= len(grid) or (j+2) >= len(grid[0]):
            return -1

        maxVal = 0 
        for row in range(i, i+3):
            for col in range(j, j+3):
                maxVal = max(maxVal, grid[row][col])
        
        return maxVal
