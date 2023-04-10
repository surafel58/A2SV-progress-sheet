class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        #adj list 
        graph = defaultdict(list)

        #dfs
        def dfs(node, visited):

            visited.add(node)
            connected.add(node)

            for neighbour in graph[node]:

                if neighbour not in visited:
                    dfs(neighbour, visited)

        #build adj list
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    graph[i + 1].append(j + 1)

        connected = set()
        count = 0

        for node in graph:
            if node not in connected:
                dfs(node, set())
                count += 1
                

        return count