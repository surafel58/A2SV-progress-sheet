class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        graph = defaultdict(list)
        
        result = [0] * n

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def dfs(node, visited):
            
            visited.add(node)
            letter_count = [0] * 26
            letter_count[ord(labels[node]) - 97] = 1

            for neighbour in graph[node]:
                if neighbour not in visited:
                    traverse = dfs(neighbour, visited)

                    for i in range(len(traverse)):
                        letter_count[i] += traverse[i]

            result[node] = letter_count[ord(labels[node]) - 97]
            return letter_count

        dfs(0, set())

        return result
