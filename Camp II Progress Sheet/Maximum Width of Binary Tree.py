# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 0, 0)])
        result = 1

        while queue:
            node, i, level = queue.popleft()

            if node.left:
                queue.append((node.left, 2*i + 1, level + 1))

            if node.right:
                queue.append((node.right, 2*i + 2, level + 1))

            if queue and queue[-1][2] == queue[0][2]:
                result = max(result, queue[-1][1] - queue[0][1] + 1)

        return result
