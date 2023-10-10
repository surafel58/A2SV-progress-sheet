class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        distances = [[float("inf")] * numCourses for _ in range(numCourses)]

        for i, j in prerequisites:
            distances[i][j] = 1

        for i in range(numCourses):
            distances[i][i] = 0

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
            

        result = [False] * len(queries)

        for i in range(len(queries)):
            row = queries[i][0]
            col = queries[i][1]
            if distances[row][col] != float('inf') and distances[row][col] > 0:
                result[i] = True
        
        return result
