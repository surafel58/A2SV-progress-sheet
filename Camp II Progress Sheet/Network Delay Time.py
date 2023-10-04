class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for time in times:
            graph[time[0]].append((time[1], time[2]))
        
        # print(graph)

        def dijkstra(graph, k):

            distances = {node : float("inf") for node in range(1, n + 1)}
            # print(distances)
            distances[k] = 0
            heap = [(0, k)]
            visited = set()

            while heap:

                curr_distance, curr_node = heapq.heappop(heap)

                if curr_node in visited:
                    continue

                visited.add(curr_node)

                for neighbour, weight in graph[curr_node]:
                    distance = curr_distance + weight

                    if distance < distances[neighbour]:
                        heapq.heappush(heap, (distance, neighbour))
                        distances[neighbour] = distance
            
            return distances

        time = dijkstra(graph, k)
        result = max(time.values()) 

        return result if result != float("inf") else -1
