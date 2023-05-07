class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def outOfBound(row, col):
            if row < 0 or row >= len(mat) or col < 0 or col >= len(mat[0]):
                return True
            return False
        
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = deque()
        visited = set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))
        level = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                for direction in directions:
                    cur_row = node[0] + direction[0]
                    cur_col = node[1] + direction[1]

                    if (cur_row, cur_col) not in visited and not outOfBound(cur_row, cur_col):
                        mat[cur_row][cur_col] = level
                        queue.append((cur_row, cur_col))
                        visited.add((cur_row, cur_col))

            level += 1

        return mat
        
