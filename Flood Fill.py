class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def outOfBound(row, col):
            
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return True
            
            return False

        def dfs(node, visited):
            
            if outOfBound(node[0], node[1]) or image[node[0]][node[1]] != image[sr][sc]:
                return
            
            visited.add(node)

            for direction in directions:
                row = node[0] + direction[0]
                col = node[1] + direction[1]

                if (row, col) not in visited:
                    traverse = dfs((row, col), visited)


        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        dfs((sr, sc), visited)

        for row, col in visited:
            image[row][col] = color

        return image
