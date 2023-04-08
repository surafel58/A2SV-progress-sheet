"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        graph = defaultdict(list)

        #adj list
        for employee in employees:
            graph[employee.id] = [employee.importance, employee.subordinates]


        total = 0
        def dfs(node, visited):
            nonlocal total

            visited.add(node)
            total += graph[node][0]

            for neighbour in graph[node][1]:
                if neighbour not in visited:
                    traverse = dfs(neighbour, visited)
        
        dfs(id, set())
        return total
