class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def outOfBound(row, col):

            if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
                return True
            
            return False

        def tracePath(pos):
            count = 0
            value = pos
            
            while path[value] != None:
                count += 1
                value = path[value]
            
            return count

        #initialization
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        m = len(maze)
        n = len(maze[0])
        
        entrance = tuple(entrance)
        
        queue = deque()
        queue.append(entrance)

        path = dict()
        path[entrance] = None
        maze[entrance[0]][entrance[1]] = 'x'

        answer = -1

        #record exits
        exits = set()
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    exits.add((i,j))
        #bfs
        while queue:

            node = queue.popleft()
            
            #if reached destination, trace path and break
            if node != entrance and node in exits:
                answer = tracePath(node)
                break
            
            for direction in directions:

                cur_row = node[0] + direction[0]
                cur_col = node[1] + direction[1]

                if not outOfBound(cur_row, cur_col) and maze[cur_row][cur_col] == '.':

                    maze[cur_row][cur_col] = 'x'
                    queue.append((cur_row, cur_col))
                    path[(cur_row, cur_col)] = (node[0], node[1])

        return answer
