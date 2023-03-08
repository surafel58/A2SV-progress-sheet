# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []
            
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            width = len(queue)
            temp = []

            for i in range(width):
                
                if queue[0].left:
                    queue.append(queue[0].left)
                
                if queue[0].right:
                    queue.append(queue[0].right)

                temp.append(queue.popleft().val)

            result.append(temp)

        return result
