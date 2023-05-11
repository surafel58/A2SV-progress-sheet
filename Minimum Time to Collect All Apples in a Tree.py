class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        graph = defaultdict(list)

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
        
        visited = set()

        #edge case
        if n == 1:
            return 0 

        def dfs(root):

            if root in visited:
                return 0

            visited.add(root)
            
            if root not in graph:
                
                if hasApple[root]:
                    return 2
                
                return 0
            
            answer = 0

            for i in graph[root]:
                answer += dfs(i)

            if answer == 0 and not hasApple[root]:
                return 0

            if root == 0:
                return answer

            return 2 + answer

        return dfs(0)  
