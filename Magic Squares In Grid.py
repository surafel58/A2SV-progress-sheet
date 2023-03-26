class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # m - 2
            # n - 2
                # check MagicSquare

        rowSize = len(grid)
        colSize = len(grid[0])
        counter = 0

        for row in range(rowSize - 2):
            for col in range(colSize - 2):
                if self.checkMagicSquare(grid, row, col):
                    counter += 1

        return counter

    def checkMagicSquare(self, grid, row, col):
        visited = set()

        #check duplicates
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if grid[i][j] in visited or not(1 <= grid[i][j] <= 9):
                    return False
                
                visited.add(grid[i][j])

        #check sum

        total = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]

        #row wise
        if total != (grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]):
            return False

        if total != (grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]):
            return False

        #col wise
        if total != (grid[row][col] + grid[row + 1][col] + grid[row + 2][col]):
            return False

        if total != (grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]):
            return False

        if total != (grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]):
            return False

        #diagonal wise
        if total != (grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]):
            return False

        if total != (grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]):
            return False


        return True


