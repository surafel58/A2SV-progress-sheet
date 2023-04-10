class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        destEdges = set()
        result = []

        for edge in edges:
            destEdges.add(edge[1])

        for i in range(n):
            if i not in destEdges:
                result.append(i) 

        return result
