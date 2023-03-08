# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return None

        result = []

        queue = deque()
        queue.append(root)

        while queue:

            width = len(queue)
            levelLastElement = 0

            for i in range(width):

                if queue[0].left:
                    queue.append(queue[0].left)

                if queue[0].right:
                    queue.append(queue[0].right)

                levelLastElement = queue.popleft()


            result.append(levelLastElement.val)
            print(levelLastElement.val)

        return result

            
