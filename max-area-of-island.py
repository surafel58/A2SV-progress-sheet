class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def outOfBound(row, col):
            
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return True
            
            return False

        def dfs(node, visited):
            nonlocal counter

            if outOfBound(node[0], node[1]) or grid[node[0]][node[1]] == 0:
                return
            
            visited.add(node)
            counter += 1

            for direction in directions:
                row = node[0] + direction[0]
                col = node[1] + direction[1]

                if (row, col) not in visited:
                    traverse = dfs((row, col), visited)


        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                counter = 0
                dfs((i, j), visited)
                result = max(result, counter) 

        return result