class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        def outOfBound(row, col):

            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid):
                return True
            
            return False

        def tracePath():
            count = 1
            value = (n - 1, n - 1)
            
            while prev[value] != None:
                count += 1
                value = prev[value]
            
            return count

        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (-1,-1), (1,-1)]

        queue = deque()
        queue.append((0,0))
        
        #base cases
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        if len(grid) == 1 and grid[0][0] == 0:
            return 1

        answer = -1
        
        #hold the parent of each node in dict to trace path
        prev = dict()
        prev[(0,0)] = None
        
        n = len(grid)
        grid[0][0] = 2

        while queue:

            node = queue.popleft()
            
            #if reached destination, trace path and break
            if (n-1, n-1) in prev:
                answer = tracePath()
                break
            
            for direction in directions:
                
                cur_row = node[0] + direction[0] 
                cur_col = node[1] + direction[1]

                if not outOfBound(cur_row, cur_col) and grid[cur_row][cur_col] == 0:

                    grid[cur_row][cur_col] = 2
                    queue.append((cur_row, cur_col))

                    prev[(cur_row, cur_col)] = (node[0], node[1])
        
        return answer




        
