class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        #dfs
        def dfs(node, visited):

            visited.add(node)

            for neighbour in graph[node]:

                if neighbour not in visited:
                    dfs(neighbour, visited)

        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                
                if i == j:
                    continue
                
                #root((x2 - x1) ^ 2 + (y2 - y1)^2)
                distance = (math.sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2))

                radius = bombs[i][2]
                if distance <= radius:
                    graph[i].append(j)
        
        visited = set()
        maxDetonation = 0

        for node in range(len(bombs)):
            visited = set()
            dfs(node, visited)
            maxDetonation = max(maxDetonation, len(visited))        

        return maxDetonation     
