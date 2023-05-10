class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        incoming = [0] * numCourses

        for prerequisite in prerequisites:
            incoming[prerequisite[0]] += 1
            graph[prerequisite[1]].append(prerequisite[0])

        queue = deque()
        order = []

        for i in range(len(incoming)):
            if incoming[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbour in graph[node]:
                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        return len(order) == numCourses
            
