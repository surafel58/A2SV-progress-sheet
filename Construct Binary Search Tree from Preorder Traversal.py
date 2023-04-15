# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# First item in preorder list is the root to be considered.
# For next item in preorder list, there are 2 cases to consider:
# If value is less than last item in stack, it is the left child of last item.
# If value is greater than last item in stack, pop it.
# The last popped item will be the parent and the item will be the right child of the parent.

class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
      root = TreeNode(preorder[0])
      stack = [root]

      for val in preorder[1:]:

        if val < stack[-1].val:

          stack[-1].left = TreeNode(val)

          stack.append(stack[-1].left)

        else:
          while stack and val > stack[-1].val:

            last_node = stack.pop()

          last_node.right = TreeNode(val)

          stack.append(last_node.right)

      return root   

