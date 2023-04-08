class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        maxNetRank = 0

        graph = defaultdict(set)

        for src, dest in roads:
            graph[src].add(dest)
            graph[dest].add(src)

        for city1 in graph:
            for city2 in graph:
                if city1 == city2:
                    continue
                
                value = len(graph[city1]) + len(graph[city2])
                
                if city2 in graph[city1]:
                    value -= 1

                maxNetRank = max(maxNetRank, value)
                
        return maxNetRank
