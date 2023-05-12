class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        queue = deque()
        graph = defaultdict(list)
        incoming = [0] * n
        ancestors = [set() for i in range(n)]
        
        for edge in edges:
            incoming[edge[1]] += 1
            graph[edge[0]].append(edge[1])

        for i in range(n):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                ancestors[neighbour] = ancestors[neighbour].union(ancestors[node])

                ancestors[neighbour].add(node)
                
                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        for i in range(n):
            ancestors[i] = sorted(ancestors[i])
        
        return ancestors
