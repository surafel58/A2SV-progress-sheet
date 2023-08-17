class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def outOfBound(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return True
            return False

        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        island = set()
        
        def dfs(node):

            island.add(node)

            for direction in directions:
                new_row = node[0] + direction[0]
                new_col = node[1] + direction[1]

                if not outOfBound(new_row, new_col) and (new_row, new_col) not in island and grid[new_row][new_col] != 0:
                    dfs((new_row, new_col))

        #collect an island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs((i, j))
                    break

            if island:
                break
            
        #do BFS starting from the first island to the second one
        queue = deque([(position[0], position[1], 0) for position in island])
        nodes = island

        while queue:
            row, col, count = queue.popleft()

            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if not outOfBound(new_row, new_col) and (new_row, new_col) not in nodes and (new_row, new_col) not in island:
                    nodes.add((new_row, new_col))
                    if grid[new_row][new_col] == 0:
                        queue.append((new_row, new_col, count + 1))
                    else:
                        return count

        return 0
