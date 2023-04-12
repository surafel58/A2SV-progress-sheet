class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def outOfBound(row, col):
            
            if row < 0 or row >= len(grid2) or col < 0 or col >= len(grid2[0]):
                return True
            
            return False

        def dfs(node, visited):

            if outOfBound(node[0], node[1]) or grid2[node[0]][node[1]] == 0:
                return
            
            visited.add(node)
            grid2[node[0]][node[1]] = 0

            for direction in directions:
                row = node[0] + direction[0]
                col = node[1] + direction[1]

                if (row, col) not in visited:
                    traverse = dfs((row, col), visited)

        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islands = []
        counter = 0

        #record grid2 islands position
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                
                if (i,j) not in visited:
                    visited = set()
                    
                    dfs((i, j), visited)

                    if len(visited) != 0:
                        islands.append(visited)

        #check if the islands in grid2 exists in the grid1 
        for island in islands:
            for pos in island:
                if not grid1[pos[0]][pos[1]]:
                    break
            else:
                counter += 1

        return counter


        
