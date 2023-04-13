class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:        
        
        def dfs(node):

            for neighbour in graph[node]:
                
                if neighbour not in color:
                    color[neighbour] = 1 - color[node]
                    traverse = dfs(neighbour)

                    if not traverse:
                        return False
                
                elif color[node] == color[neighbour]:
                    return False
            
            return True
        

        graph = defaultdict(list)
        color = dict()

        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        for node in graph:
            if node not in color:
                
                color[node] = 0
                result = dfs(node)
                
                if not result:
                    return False
        return True

        
