class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = defaultdict(list)

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        def dijkstra(graph, src, dest, k):

            distances = [float("inf")] * n
            heap = [(-1, 0, src)]

            while heap:
                stops, curr_distance, curr_node = heapq.heappop(heap)
                
                if (stops == k + 1) or curr_distance >= distances[curr_node]:
                    continue

                distances[curr_node] = curr_distance
                        
                for neighbour, weight in graph[curr_node]:
                    distance = curr_distance + weight

                    heapq.heappush(heap, ( stops + 1, distance, neighbour))

            return -1 if distances[dest] == float('inf') else distances[dest]

        return dijkstra(graph, src, dst, k)
