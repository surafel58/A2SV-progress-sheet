class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if "0000" in deadends:
            return -1

        if "0000" == target:
            return 0

        initial_node = ["0000", 0]
        
        queue = deque([initial_node])

        visited = set()

        result = 0

        while queue:

            node, level = queue.popleft()
            node = list(map(int, node))
            n = len(node)

            for i in range(n):
                new_node_1 = node.copy()
                new_node_1[i] = (new_node_1[i] + 1) % 10

                new_node_2 = node.copy()
                new_node_2[i] = (new_node_2[i] - 1) % 10
                
                temp_1 = "".join(map(str, new_node_1))
                temp_2 = "".join(map(str, new_node_2))

                if temp_1 not in visited and temp_1 not in deadends:
                    queue.append([temp_1, level + 1])
                    visited.add(temp_1)

                    if temp_1 == target:
                        return level + 1
                    
                if temp_2 not in visited and temp_2 not in deadends:
                    queue.append([temp_2, level + 1])
                    visited.add(temp_2)

                    if temp_2 == target:
                        return level + 1

        return -1
