class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def outOfBound(row, col):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return True

            return False

        def dfs(node, visited):

            if outOfBound(node[0], node[1]):
                return True

            if board[node[0]][node[1]] == 'X':
                return False

            visited.add(node)

            for direction in directions:
                
                new_row = node[0] + direction[0] 
                new_col = node[1] + direction[1]

                if (new_row, new_col) not in visited:

                    traverse = dfs((new_row, new_col), visited)

                    if traverse:
                        return True

            return False

        discovered = set()

        for row in range(len(board)):
            for col in range(len(board[0])):

                if board[row][col] != 'X': 
                    visited = set()

                    if not dfs((row, col), visited) and (row, col) not in discovered:

                        for pos in visited:
                            board[pos[0]][pos[1]] = 'X'
                        
                        discovered = discovered | visited
                        
                    
