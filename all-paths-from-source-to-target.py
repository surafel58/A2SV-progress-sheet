class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        path = []
        n = len(graph)

        def dfs(node, visited):
            
            path.append(node)

            if node == (n - 1):
                    
                result.append(path.copy())
                path.pop()
                return

            visited.add(node)

            for neighbour in graph[node]:

                if neighbour not in visited:
                    dfs(neighbour, visited) 

            #pop the current node whne backtracking
            path.pop()
            visited.remove(node)


        dfs(0, set())

        return result