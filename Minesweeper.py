class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        directions = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]

        def outOfBound(row, col):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return True

            return False
        
        def dfs(node, visited):
            
            visited.add(node)

            #count adjacent mine if there exist and return
            counter = 0
            for direction in directions:
                new_row = node[0] + direction[0]
                new_col = node[1] + direction[1]

                if not outOfBound(new_row, new_col) and board[new_row][new_col] == 'M':
                    counter += 1
            
            #mark the cell the number of mines adjacent to it
            if counter > 0:
                board[node[0]][node[1]] = str(counter)
                return

            # print(node[0], node[1])
            board[node[0]][node[1]] = 'B'
            for direction in directions:

                new_row = node[0] + direction[0]
                new_col = node[1] + direction[1]

                if (new_row, new_col) not in visited and not outOfBound(new_row, new_col):
                    
                    traverse = dfs((new_row, new_col), visited)

        
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        
        else:
            dfs((click[0], click[1]), set())

            
        return board

       


