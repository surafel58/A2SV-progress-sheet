class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        solution = set(edges[0])
        for e in edges:
            solution = solution.intersection(e)

        return list(solution)[0]
