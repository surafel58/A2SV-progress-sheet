# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        if k == 0:
            return [target.val]

        adjList = defaultdict(list)

        def getAdjList(adjList, root):

            if root:
                if root.left: 
                    adjList[root.val].append(root.left.val)
                    adjList[root.left.val].append(root.val)
                    getAdjList(adjList, root.left)
            
                if root.right:
                    adjList[root.val].append(root.right.val)
                    adjList[root.right.val].append(root.val)
                    getAdjList(adjList, root.right)

        #get adj list
        getAdjList(adjList, root)

        #bfs
        queue = deque([(target.val, 0)])
        visited = set([target.val])
        result = []

        while queue:
            node, count = queue.popleft()
            
            for neighbour in adjList[node]:
                if neighbour not in visited:
                    if (count + 1) == k:
                        result.append(neighbour)

                    queue.append((neighbour, count + 1))
                    visited.add(neighbour)
        
        return result
            
