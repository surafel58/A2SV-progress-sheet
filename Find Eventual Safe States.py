class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        colors = [0] * n
        safe_nodes = []

        def dfs(node):
            
            if colors[node] == 1:
                return True
            
            colors[node] = 1

            for neighbour in graph[node]:

                if colors[neighbour] != 2:

                    if dfs(neighbour):
                        return True
            
            colors[node] = 2
            safe_nodes.append(node)
            return False

        for i in range(n):
            if colors[i] != 2:
                dfs(i)

        return sorted(safe_nodes)
